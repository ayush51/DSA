def __init__(self):
    self.numMap = {}
    self.numListt = []
def insert(self, val:int)->bool:
    res = val not in self.numMap: #if val not in map
        if res:
            self.numMap[val]=len(self.numList)
            self.numList.appen[val]
        return res
def remove(self, val: int)->bool:
    res = val in self.numMap #if val in map
    if res:
        idx = self.numMap[val]
        lastval = self.numList[-1]   #intro lastval cz popping it in 0(1)
        self.numList[idx] = lastval
        self.numList.pop()
        self.numMap[lastval] = idx
        del self.numMap[val]
    return res
 def getrandom(self)->int:
   return random.choice(self.numList)
        
