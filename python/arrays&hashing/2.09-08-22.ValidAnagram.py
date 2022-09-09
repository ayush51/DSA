class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        #builidng the hasmap and getting the occurence of each character in the strings
        
        for i in range (len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            #Using the get function to actually put defualt value zero in case S[I] doesn;t exist more than once in s
            #ITERATING THROUGH THE HASHMAP
            
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True;

    
    
    ### way 2 
    
    #sort the strings and compare
    
    code:
        
        return sorted(s) = sorted(t) 
    
    way 3:
        
        return Counter(s) = Counter(t)
    
    
    
