import cv2

class HUDRenderer:
    @staticmethod
    def draw(frame, state, landmarks, w, h):
        # 1. Draw Attention Bar at the top
        bar_w, bar_h = 300, 20
        cv2.rectangle(frame, (20, 20), (20 + bar_w, 20 + bar_h), (50, 50, 50), -1)
        fill_w = int((state["attention"] / 100) * bar_w)
        
        # Green if high, Red if low
        color = (0, 255, 0) if state["attention"] > 60 else (0, 0, 255)
        cv2.rectangle(frame, (20, 20), (20 + fill_w, 20 + bar_h), color, -1)
        cv2.putText(frame, f"ATTENTION: {state['attention']}%", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # 2. Draw Text States
        y_offset = 95
        for key, val in state.items():
            if key in ["ear", "attention"]: continue
            c = (0, 255, 0) if val in ["CENTER", "FRONT", "ALERT"] else (0, 100, 255)
            cv2.putText(frame, f"{key.upper()}: {val}", (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, c, 2)
            y_offset += 30

        # 3. HIGHLY VISIBLE PUPIL TRACKING
        # Get exact pixel coordinates of the center of the pupils
        left_pupil_x = int(landmarks[468].x * w)
        left_pupil_y = int(landmarks[468].y * h)
        
        right_pupil_x = int(landmarks[473].x * w)
        right_pupil_y = int(landmarks[473].y * h)

        # Draw a large bright green circle around the pupil
        cv2.circle(frame, (left_pupil_x, left_pupil_y), 10, (0, 255, 0), 2)
        cv2.circle(frame, (right_pupil_x, right_pupil_y), 10, (0, 255, 0), 2)
        
        # Draw a small red dot exactly in the middle of the pupil
        cv2.circle(frame, (left_pupil_x, left_pupil_y), 2, (0, 0, 255), -1)
        cv2.circle(frame, (right_pupil_x, right_pupil_y), 2, (0, 0, 255), -1)