class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)-2):
            for j in range(i+1, len(temperatures)-1):
                if temperatures[i] < temperatures[j]:
                    res[i] = (j-i)
                    break
                
        return res
        
