class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int K = 0;
        for(int i : nums){
            if(i!=val)
                nums[K++] = i;
        }
        return K;
    }
};


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k=0;
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i];
                k+=1;
        return k;
        
