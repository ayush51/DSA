class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #for i in range(0, len(arr)):
        i=0;
        while i < len(arr) - 1:
            if arr[i] == 0:
               # for j in range(len(arr), i):
                 #   arr[j+1]=nums[j];
                  #  arr[j] = 0;
                arr.pop();
                arr.insert(i+1,0);
                i+=1;
            i+=1;
