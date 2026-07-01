import numpy as np
from collections import deque

class GazeTracker:
    def __init__(self, buffer_size=5):
        self.h_smoother = deque(maxlen=buffer_size)
        self.v_smoother = deque(maxlen=buffer_size)

    def get_state(self, lm, w, h):
        # --- HORIZONTAL GAZE ---
        raw_gaze_h = ((lm[468].x - lm[33].x)/(lm[133].x - lm[33].x + 1e-6) + 
                      (lm[473].x - lm[362].x)/(lm[263].x - lm[362].x + 1e-6)) / 2
        self.h_smoother.append(raw_gaze_h)
        avg_h = np.mean(self.h_smoother)

        # --- VERTICAL GAZE (Looking up/down) ---
        l_eye_center_y = (lm[159].y + lm[145].y) / 2
        r_eye_center_y = (lm[386].y + lm[374].y) / 2
        
        raw_gaze_v = ((lm[468].y - l_eye_center_y) / (lm[145].y - l_eye_center_y + 1e-6) + 
                      (lm[473].y - r_eye_center_y) / (lm[374].y - r_eye_center_y + 1e-6)) / 2
        self.v_smoother.append(raw_gaze_v)
        avg_v = np.mean(self.v_smoother)

        # --- DIRECTIONS ---
        # If pupil goes towards outer corner (lower number), you are looking RIGHT
        h_state = "CENTER"
        if avg_h < 0.40: h_state = "RIGHT"
        elif avg_h > 0.60: h_state = "LEFT"

        v_state = ""
        if avg_v < -0.1: v_state = "UP"
        elif avg_v > 0.8: v_state = "DOWN"

        # Combine them
        if h_state == "CENTER" and v_state == "":
            return "CENTER"
        elif v_state != "":
            return f"{v_state}-{h_state}".strip("-")
        else:
            return h_state