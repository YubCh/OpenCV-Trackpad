from hand_tracker import get


#     return in [thumb, index, middle, ring, pinky] form
# this is the index of position[finger][x/y] x-0 y-1
# 	            Thumb	Index	Middle	Ring	Pinky
# tip	            4	    8	    12	  16	    20
# joint below tip	3	    7	    11	  15	    19
# middle joint	  2	    6	    10  	14	    18
# base knuckle	  1	    5	     9	  13	    17
# 0 = wrist

class GestureRecognizer:


  def fingers_up(self, positions, is_left):
    res = [0,0,0,0,0]
    if is_left:
      if position[4][0] < position[3][0] and position[4][0] < position[2][0]:
        res = [1,0,0,0,0]
      elif position[4][0] > position[3][0] and position[4][0] > position[2][0]:
        res = [1,0,0,0,0]
    for i in range(8, len(positions),4):
      if positions[i][1] > positions[i - 1][1] or positions[i][1] > positions[i - 2][1]:
        res[(i/4) - 1] = True
      else:
        res[(i/4) - 1] = False 
    return res
