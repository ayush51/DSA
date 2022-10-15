class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.nums = []
        
        for i, num in enumerate(nums):
            if num:  #append if num! = 0
                self.nums.append((i,num))
     

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotP = 0
        i = j = 0
        
        while i < len(self.nums) and j < len(vec.nums):
            i_idx, i_num = self.nums[i]
            j_idx, j_num = vec.nums[j]
            
            if i_idx == j_idx:
                dotP += (i_num * j_num)
                
                i += 1
                j += 1 
                
            elif i_idx > j_idx:
                j += 1
                
            else:
                i += 1
            
        return dotP

                
# [<0,1>, <3,2>, <4:3>] = nums
#[<1,3>, <3,4>] = vec
#
#i = 0, j = 0
#
#self.nums[0] = 0,1
#vec.nums[0] = 1,3
#
#
#i_idx = 0
#j_idx = 1
#
#so i_idx < j_idx
# hence i += 1
#

# i = 1,  j = 0
#
#self.nums[1] = <3,2>
#vec.nums[0] = 1, 3
#
#so i_idx > j_idx
# hence j += 1

# i = 1, j = 1
#
#self.nums[1] = 3,2
#vec.nums[1] = 3, 4
#
# so i_idx == j_idx
#hence dotP = inum* jnum = 2 * 4 = 8
#i += 1, j += 1

# i = 2, j = 2 (exceeding len of vec - hence won't enter while loop and return dotP
#

# TC : O(m+n)---- looping through nums to append non zero elements to tuple
# SC : O(m+n)---- adding to tuple




#
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
