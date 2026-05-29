#include <set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        std::set<int> seen = {};

        for (int i = 0; i < nums.size(); i++) {
            if (seen.find(nums[i]) == seen.end()) {
                seen.insert(nums[i]);
            } else {
                return true;
            }
        }
        return false;
    }
};