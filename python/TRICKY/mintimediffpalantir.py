class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def toMin(time):
            time = time.split(":")
            res = (60*int(time[0]) + int(time[1])
            return res
                   
        for i, time in enumerate(timePoints):
            timePoints[i] = toMin(time)
        
        res = sys.maxsize
        timePoints.sort()
        for i in range(0,len(times)-1):
            res = min(res, (timePoints[i+1] - timePoints[i]))  
        res = min(res, 60*24 - timePoints[-1] + timePoints[0])
        return res
        
        
