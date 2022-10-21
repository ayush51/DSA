class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res[i] = (j-i)
                    break
                
        return res
    
    
    O(n)
    
    class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack = [] #temp, indexoftemp : calc the no of days for greater temp
        
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #stack non empty  and stack top is LESS than temp
                stackT, stackI = stack.pop()       #then pop from stack and we calc index - stackI AND APPEND TO RES
                res[stackI] = (i-stackI)
            stack.append([t,i])
        
        
                
        return res
        
        
