def recursiveCall(c, x1, y1, x2, y2):
  if x2 < x1 or y2< y1: return False
  a = math.sqrt(x1 + y1)
  b = a - math.floor(a)
  if b== 0: return False
  if x1 == x2 and y1 == y2 return True
check = recursivecall(c, x1+y1, y1, x2, y2) or recall(c, x1+c, y1+c, x2, y2) or recall(c, x1, x1+y1, x2, y2)
return check

def canreach (c, x1, x2, y1, y2)
check = helper (c, x1, y1, x2, y2)
if check: return Yes
return No
