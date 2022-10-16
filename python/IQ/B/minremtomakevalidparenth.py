class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l_count = r_count = 0
        
        res = []
        
        for c in s:
            if c == "(":
                l_count += 1
                res.append(c)
            elif c == ")":
                if l_count > r_count:
                    r_count += 1 
                    res.append(c)
            else:
                res.append(c)  #if they are lowercase
            
        if l_count == r_count: #i.e number of left parenthesis quals to right
            return "".join(res)
        
        else:
            result = []
            
            for i in range(len(res)-1,-1,-1):
                curr_char = res[i]
                
                if curr_char == "(":
                    if l_count <= r_count:
                        result.append(curr_char)
                    else:
                        l_count -= 1
                #elif curr_char = ")":
                 #   result.append(curr_char)
                else:
                    result.append(curr_char)
                    
            return "".join(reversed(result))
        
        
