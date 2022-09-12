class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #building hashmap (default dict) for key value
        for s in strs:
            count = [0] * 26 # a-z
            for c in s:
                count[ord(c)-ord("a")] +=1 
                  #for associating a to 0 and z to 25, we use ASCII and count
                
            res[tuple(count)].append(s) 
        
              #to group tgether all the anagrams (strings) that are anagrams
            
        return res.values()
