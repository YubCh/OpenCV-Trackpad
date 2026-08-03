import cv2
import mediapipe as mp
import time
from camera import Camera
from hand_tracker import HandTracker
from gesture import GestureRecognizer




if __name__ == "__main__":
    hand_tracker = HandTracker()
    gesture = GestureRecognizer()
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
       print(gesture.fingers_up(hand_tracker.get_positions(frame), hand_tracker.is_left_hand()))
       print(int(gesture.distance(hand_tracker.get_positions(frame), 4, 8)))
       if cv2.waitKey(1) == ord('q'):
        break
    cam.release()
    cv2.destroyAllWindows()