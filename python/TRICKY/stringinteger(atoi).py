class Solution:
    def myAtoi(self, s: str) -> int:

        
        
        
        #strip leading whitespaces
        #check if string is empty ot contains anything
        #check for positive or negative 
        #parse any digits 1 by 1
        #check if num in between signed integer range
        
        s = s.lstrip()  #O(N)
        
        
        #check another edge case -- if its an empty string
        
        if not s:
            return 0
        
        #do awhile loop and parse index by index
        
        
        #check if positive or negative sign
        i = 0
        
        sign = 1 #flag to signify +ve else -
        
        if s[i] == '+':
            i += 1
        if s[i] == '-':
            i += 1
            sign = -1
        if i == 2:
            return 0
                
                
            #start parsing digits
            
        parsed = 0
        while i < len(s):  #O(N)
            curr = s[i]
            
            if not curr.isdigit():
                break
            else:
                parsed = parsed * 10 + int(curr)
                
            i += 1
            
        parsed *= sign
        
               #check if parsed in signed integer rage
            
        if parsed > 2**31 - 1:
            return 2**31 - 1
        elif parsed <= -2**31:
            return -2**31
        else:
            return parsed
            
            
#TC  O(n), SC = O(1)
        
        
        
                
            
        
