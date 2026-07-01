import numpy as np
from collections import deque

class FatigueTracker:
    def __init__(self, buffer_size=5, ear_threshold=0.2):
        self.smoother = deque(maxlen=buffer_size)
        self.ear_threshold = ear_threshold

    @staticmethod
    def _dist(p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2))

    def get_state(self, lm, w, h):
        # Left Eye
        l_top, l_bot = (lm[159].x*w, lm[159].y*h), (lm[145].x*w, lm[145].y*h)
        l_left, l_right = (lm[33].x*w, lm[33].y*h), (lm[133].x*w, lm[133].y*h)
        ear_l = self._dist(l_top, l_bot) / (self._dist(l_left, l_right) + 1e-6)

        # Right Eye
        r_top, r_bot = (lm[386].x*w, lm[386].y*h), (lm[374].x*w, lm[374].y*h)
        r_left, r_right = (lm[362].x*w, lm[362].y*h), (lm[263].x*w, lm[263].y*h)
        ear_r = self._dist(r_top, r_bot) / (self._dist(r_left, r_right) + 1e-6)
        
        ear = (ear_l + ear_r) / 2.0
        self.smoother.append(ear)
        avg_ear = np.mean(self.smoother)

        if avg_ear < self.ear_threshold: return "DROWSY", avg_ear
        return "ALERT", avg_ear