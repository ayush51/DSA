class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for st, en in intervals:
            start += [st]
            end += [en]
        
        start.sort()
        end.sort()
        
        res, count  = 0, 0
        s, e = 0, 0 
        
        while s<len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1 
            else:
                e+= 1
                count -= 1
            res = max(count, res)
        return res



















start = sorted([i.start for i in intervals])
end = sorted([e.start for e in intervals])

res, count = 0, 0
s,e = 0,0

while s<len(intervals):
  if start[s]<end[e]
      s+=1
      count +=1
      
  else: 
    e+=1
    count -=1
    
    res = max(res, count)
    
    ret res
