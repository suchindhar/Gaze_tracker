from .gaze import GazeTracker
from .pose import PoseTracker
from .fatigue import FatigueTracker

class AttentionEngine:
    def __init__(self):
        self.gaze = GazeTracker(buffer_size=7)
        self.pose = PoseTracker(buffer_size=7)
        self.fatigue = FatigueTracker(buffer_size=7)
        self.attention_score = 100.0

    def process(self, landmarks, w, h):
        # 1. Get raw states from sub-modules
        gaze_state = self.gaze.get_state(landmarks, w, h)
        head_state = self.pose.get_state(landmarks, w, h)
        fatigue_state, ear_val = self.fatigue.get_state(landmarks, w, h)

        # 2. Calculate Penalty
        target_score = 100
        if gaze_state != "CENTER": target_score -= 30
        if head_state != "FRONT": target_score -= 40
        if fatigue_state == "DROWSY": target_score -= 50
        
        # 3. Smoothly adjust the 0-100 score
        self.attention_score += (target_score - self.attention_score) * 0.1

        return {
            "gaze": gaze_state,
            "head": head_state,
            "fatigue": fatigue_state,
            "ear": ear_val,
            "attention": int(self.attention_score)
        }