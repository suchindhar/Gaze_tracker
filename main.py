import cv2
import time
import pathlib
import pyautogui
import mediapipe as mp  
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from analyzer import AttentionEngine
from ui import HUDRenderer

pyautogui.FAILSAFE = False 

def main():
    SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
    MODEL_PATH = SCRIPT_DIR / "models" / "face_landmarker.task"
    
    base_options = python.BaseOptions(model_asset_path=str(MODEL_PATH))
    options = vision.FaceLandmarkerOptions(base_options=base_options, num_faces=1)
    detector = vision.FaceLandmarker.create_from_options(options)

    engine = AttentionEngine()
    renderer = HUDRenderer()
    
    cap = cv2.VideoCapture(0)
    last_focus_time = time.time()

    print("Starting NeuroTrack... Press ESC to exit!")
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success: break
        
        # 1. FLIP IMMEDIATELY. Now it's a mirror. Text will draw normally on the left side.
        frame = cv2.flip(frame, 1) 
        h, w, _ = frame.shape
        
        # 2. Convert for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        result = detector.detect(mp_image)
        
        if result.face_landmarks:
            # 3. Analyze
            state = engine.process(result.face_landmarks[0], w, h)
            
            # 4. Draw UI (Will appear correctly on the left, right-side up)
            renderer.draw(frame, state, result.face_landmarks[0], w, h)

            # 5. Auto-Pause Logic
            if state["attention"] < 30:
                if time.time() - last_focus_time > 3.0:
                    pyautogui.press('space') 
                    last_focus_time = time.time()
                    cv2.putText(frame, "AUTO-PAUSED", (50, h//2), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            else:
                last_focus_time = time.time()

        # NO FLIP HERE. Just show the frame.
        cv2.imshow('NeuroTrack: Cognitive Analyzer', frame)
        
        # Press ESC to quit (ASCII code 27)
        if cv2.waitKey(1) == 27: break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()