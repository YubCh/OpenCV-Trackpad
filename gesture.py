


#     return in [thumb, index, middle, ring, pinky] form
# this is the index of position[finger][x/y] x-0 y-1
# 	            Thumb	Index	Middle	Ring	Pinky
# tip	            4	    8	    12	  16	    20
# joint below tip	3	    7	    11	  15	    19
# middle joint	  2	    6	    10  	14	    18
# base knuckle	  1	    5	     9	  13	    17
# 0 = wrist

def fingers_up(position):
  res = [0,0,0,0,0]
  for i in range(4,len(positions),4):
    if position[i][0] > position[i - 1][0] or position[i][0] > position[i - 2][0]:
      res[(i/4) - 1] = True
    else:
      res[(i/4) - 1] = False
  return res
