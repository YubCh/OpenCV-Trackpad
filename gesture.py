import math


#     return in [thumb, index, middle, ring, pinky] form
# this is the index of position[finger][x/y] x-0 y-1
# 	            Thumb	Index	Middle	Ring	Pinky
# tip	            4	    8	    12	  16	    20
# joint below tip	3	    7	    11	  15	    19
# middle joint	  2	    6	    10  	14	    18
# base knuckle	  1	    5	     9	  13	    17
# 0 = wrist

class GestureRecognizer:

  def __init__(self):
    self.left_pinch_active = False
    self.right_pinch_active = False


  def fingers_up(self, positions, is_left):
    res = [0,0,0,0,0]
    if not positions:
      return res
    #thumb
    if is_left and positions[4][0] > positions[3][0] and positions[4][0] > positions[2][0]:
        res[0] = 1
    elif not is_left and positions[4][0] < positions[3][0] and positions[4][0] < positions[2][0]:
        res[0] = 1
    #rest
    for i in range(8, len(positions),4):
      if positions[i][1] > positions[i - 1][1] or positions[i][1] > positions[i - 2][1]:
        res[int(i/4) - 1] = 0
      else:
        res[int(i/4) - 1] = 1 
    return res

  def distance(self, positions, idx_a, idx_b):
    if not positions:
      return 0
    x1, y1 = positions[idx_a][0],positions[idx_a][1]
    x2, y2 = positions[idx_b][0],positions[idx_b][1]
    return math.hypot(x1 - x2, y1 - y2)
  
  def detect(self, positions, is_left):
    if not positions:
      return ("idle", None)
    fingers = self.fingers_up(positions, is_left)
    dist_thumb_index = self.distance(positions,4,8)
    dist_thumb_middle = self.distance(positions,4,12)
    self.left_pinch_active = False
    self.right_pinch_active= False

    if dist_thumb_index < 50 and fingers[2] == 1:
      self.left_pinch_active = True
      return ("left", positions[8])
    elif dist_thumb_middle < 50 and fingers[1] == 1:
      self.right_pinch_active = True
      return ("right", positions[12])
    elif fingers == [0,1,1,0,0]:
      return ("move", positions[8])
    return ("idle", None)  

  


