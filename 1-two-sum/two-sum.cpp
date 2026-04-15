#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Map to store: {value, index}
        std::unordered_map<int, int> numMap;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            // Check if the complement exists in our map
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            
            // If not found, add current number and its index to the map
            numMap[nums[i]] = i;
        }
        
        // Return empty if no solution is found
        return {};
    }
};