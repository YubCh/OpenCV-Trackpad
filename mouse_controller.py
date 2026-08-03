import pyautogui
import numpy as np


class MouseController:
  def __init__(self, cam_width, cam_height, margin=200):
    self.screen_w, self.screen_h = pyautogui.size()
    self.cam_w = cam_width
    self.cam_h = cam_height
    self.margin = margin
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True

  def move(self, position):
    x = position[0]
    y = position[1]

    fx = (x - self.margin) / (self.cam_w - 2 * self.margin)
    fy = (y - self.margin) / (self.cam_h - 2 * self.margin)

    fx = np.clip(fx, 0, 1)
    fy = np.clip(fy, 0, 1)

    screen_x = fx * self.screen_w
    screen_y = fy * self.screen_h

    pyautogui.moveTo(screen_x, screen_y)