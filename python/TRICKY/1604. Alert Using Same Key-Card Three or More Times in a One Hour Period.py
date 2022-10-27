import collections
from collections import deque


input1 = ["daniel","daniel","daniel","luis","luis","luis","luis"]
input2 = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]


def alertNames(keyName, keyTime):
        
    n = len(keyName)
    
    times = collections.defaultdict(list)
    
    for i in range(n):
        name = keyName[i]
        time = keyTime[i]
        
        t = time.split(":")
        
        h = int(t[0])
        m = int(t[1])
        
        times[name].append(h*60+m)
        
    #print(times)
    
    ans = []
    
    for name in times:
        time_list = sorted(times[name])
        #print(time_list)
        
        queue = collections.deque()
        
        for time in time_list:
            queue.append(time)
            #print(queue)
            
            
            while time - queue[0] > 60:
                queue.popleft()
                #print(queue)
                
            if len(queue) >= 3:
                ans.append(name)
                break
                    
    return sorted(ans)
                    
print(alertNames(input1,input2))
            
    
#TC O(NLOGN)
#SC O(N)
    
        
