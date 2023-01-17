class Solution:
    def pairofsongs(self, time: List[int]) -> int:
        pairs = 0 #this is the result 
       
        durationofsongs = collections.defaultdict(int)  #creating a dict where key is the remainder and value is the count each time that remainder comes when % with 60
        
        
        for song_length in time:
            remainder = song_length%60
          
          #if remainder 0 then all those songslengths which have remainder 0(already stored in dict) will be added to pairs 
          
            if remainder == 0:
                pairs += durationofsongs[0]
            else:
                pairs += durationofsongs[60-(song_length%60)]
             durationofsongs[song_length%60] += 1
            
         return pairs
           
