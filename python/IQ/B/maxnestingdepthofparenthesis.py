class Solution:
    def maxDepth(self, s: str) -> int:
        
        #i want to go through the strings
        #i want to count all the parenthesis
        #i want to create a new variable to count the parenthesis
        #i'll create another variable for max num
        #i want to count open parenthesis but if i close it we also sub count for that closing bracket
        
        count = 0
        maxnum = 0
        for i in s:
            if i == "(":
                count += 1
                
            if i == ")":
                count -= 1
            maxnum = max(count, maxnum)
        return maxnum
                
        
        
