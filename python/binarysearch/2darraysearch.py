class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        
        rows = len(matrix)
        cols = len(matrix[0])
        
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = (top + bottom)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        if not(top<=bottom):
            return False
                
        mid = (top + bottom)//2
        i, j  = 0, cols-1
        
        while i <= j:
            midc = (i+j)//2
            if target == matrix[mid][midc]:
                return True
            elif target > matrix[mid][midc]:
                i = midc + 1
            else:
                j = midc - 1
        return False
                    
        
