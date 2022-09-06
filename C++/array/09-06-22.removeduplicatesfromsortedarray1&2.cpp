class Solution {
public:
    int removeDuplicates(vector<int>& nums){
        if (nums.size()==0)
            return 0;
        
        int i = 0;
        for(int j =1 ; j<nums.size(); j++){
            if(nums[j] != nums[i]){
                i++;
                    nums[i]=nums[j];
            }
        }
        return i+1;
    }
};

/////////////////////////


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()==0) return 0;
        int i = 0;
        for(auto e:nums){
            if(i==0|| i==1|| nums[i-2]!=e){
                nums[i]=e;
                i++;
            }
        }
        return i;
    }
};

=======================================
    
    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0;
        for i in range (1, len(nums)):
            if nums[i]!=nums[j]:
                j+=1;
                nums[j]=nums[i];
        return j+1;
        
