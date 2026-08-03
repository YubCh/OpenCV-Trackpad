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
    self.prev_x = None
    self.prev_y = None

  def move(self, position):
    x = position[0]
    y = position[1]

    fx = (x - self.margin) / (self.cam_w - 2 * self.margin)
    fy = (y - self.margin) / (self.cam_h - 2 * self.margin)

    fx = np.clip(fx, 0, 1)
    fy = np.clip(fy, 0, 1)

    screen_x = fx * self.screen_w
    screen_y = fy * self.screen_h

    if self.prev_x is not None:
      screen_x = self.prev_x + (screen_x - self.prev_x) * 0.3
      screen_y = self.prev_y + (screen_y - self.prev_y) * 0.3
    
    self.prev_x, self.prev_y = screen_x, screen_y
    pyautogui.moveTo(screen_x, screen_y)

  def click(self, button):
    pyautogui.click(button=button)
