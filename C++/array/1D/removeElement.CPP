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
