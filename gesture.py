


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
    if not positions:
      return res
    if is_left and positions[4][0] > positions[3][0] and positions[4][0] > positions[2][0]:
        print("left hand rn")
        res[0] = 1
    elif not is_left and positions[4][0] < positions[3][0] and positions[4][0] < positions[2][0]:
        print("right hand rn")
        res[0] = 1
    for i in range(8, len(positions),4):
      if positions[i][1] > positions[i - 1][1] or positions[i][1] > positions[i - 2][1]:
        res[int(i/4) - 1] = 0
      else:
        res[int(i/4) - 1] = 1 
    return res
