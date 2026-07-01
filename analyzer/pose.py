import numpy as np
from collections import deque

class PoseTracker:
    def __init__(self, buffer_size=5):
        self.h_smoother = deque(maxlen=buffer_size)
        self.v_smoother = deque(maxlen=buffer_size)

    def get_state(self, lm, w, h):
        # --- HORIZONTAL HEAD (Yaw) ---
        raw_head_h = (lm[1].x - lm[234].x) / (lm[454].x - lm[234].x + 1e-6)
        self.h_smoother.append(raw_head_h)
        avg_h = np.mean(self.h_smoother)

        # --- VERTICAL HEAD (Pitch) ---
        raw_head_v = (lm[1].y - lm[10].y) / (lm[152].y - lm[10].y + 1e-6)
        self.v_smoother.append(raw_head_v)
        avg_v = np.mean(self.v_smoother)

        # --- DIRECTIONS ---
        # If nose goes towards right ear (higher number), you are turning RIGHT
        h_state = "FRONT"
        if avg_h < 0.40: h_state = "LEFT"
        elif avg_h > 0.60: h_state = "RIGHT"

        v_state = ""
        if avg_v < 0.40: v_state = "UP"
        elif avg_v > 0.65: v_state = "DOWN"

        # Combine them
        if h_state == "FRONT" and v_state == "":
            return "FRONT"
        elif v_state != "":
            return f"{v_state}-{h_state}".replace("FRONT", "").strip("-")
        else:
            return h_state