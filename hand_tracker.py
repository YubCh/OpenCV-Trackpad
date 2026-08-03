import cv2
import mediapipe as mp
import time
from camera import Camera

class HandTracker:
  def __init__(self, model_path="hand_landmarker.task", max_hands=1, detection_conf=0.7, tracking_conf=0.5):
    base_option = mp.tasks.BaseOptions(model_asset_path=model_path)
    landmarker_option = mp.tasks.vision.HandLandmarkerOptions(
      base_options = base_option,
      running_mode=mp.tasks.vision.RunningMode.VIDEO,
      num_hands=max_hands,
      min_hand_detection_confidence=detection_conf,
      min_tracking_confidence=tracking_conf,
      )
    self.result = None
    self.landmarker = mp.tasks.vision.HandLandmarker.create_from_options(landmarker_option)

  def find_hand(self, frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    timestamp = int(time.time() * 1000)
    self.result = self.landmarker.detect_for_video(mp_image, timestamp)
  
  def draw_landmarks(self, frame):
    h, w = frame.shape[:2]
    if not self.result or not self.result.hand_landmarks:
      return frame
    for hand in self.result.hand_landmarks:
      for landmark in hand: 
        x = int(landmark.x * w)
        y = int(landmark.y * h)
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
    return frame
  
  def get_positions(self, frame):
    h, w = frame.shape[:2]
    if not self.result or not self.result.hand_landmarks:
      return []
    hand = self.result.hand_landmarks[0]
    return [(int(lm.x * w), int(lm.y * h)) for lm in hand]

  def is_left_hand(self):
    if not self.result or not self.result.handedness:
        return False
    return not self.result.handedness[0][0].category_name == "Left"


if __name__ == "__main__":
    hand_tracker = HandTracker()
    cam = Camera()
    print("camera opened")
    while True:
       ret, frame = cam.get_frame()
       if not ret:
          print("Can't receive frame (stream end?). Exiting ...")
          break
       hand_tracker.find_hand(frame)
       frame = hand_tracker.draw_landmarks(frame)
       cv2.imshow("Trackpad", frame)
       print(f"is left? {hand_tracker.is_left_hand()}")
       print(gesture.fingers_up(hand_tracker.get_positions, HandTracker.is_left_hand))
       if cv2.waitKey(1) == ord('q'):
        break
    cam.release()
    cv2.destroyAllWindows()