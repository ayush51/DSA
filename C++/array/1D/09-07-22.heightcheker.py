class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h1 = sorted(heights)
        count = 0
        for i in range (len(heights)):
            if h1[i]!=heights[i]:
                count+=1
        return count
        
