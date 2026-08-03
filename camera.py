import numpy as np
import cv2



class Camera:

  #TODO somehow sometimes my iphone camera turns on. Need to do something with camera_index
  def __init__(self, camera_index=0, width=640, height=480):
    self.cap = cv2.VideoCapture(camera_index)
    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    if self.cap.isOpened():
       print(True)
    else:
       raise RuntimeError("Camera Not Found")

  def get_frame(self):
     success, frame = self.cap.read()
     horizontal_flip = cv2.flip(frame, 1) - 1
     return success, horizontal_flip if success else None

  def release(self):
     self.cap.release()





if __name__ == "__main__":
    cam = Camera()
    print("camera opened")
    while True:
       ret, frame = cam.get_frame()

       if not ret:
          print("Can't receive frame (stream end?). Exiting ...")
          break
       cv2.imshow("Trackpad", frame)
       if cv2.waitKey(1) == ord('q'):
          break
       cv2.destroyAllWindows()
       