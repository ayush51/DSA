class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #initialize rightmax = -1
        #reverse iteration
        #logic newMax = max(oldmax, arr[i])
        rightMax = -1
        for i in range (len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr
        
