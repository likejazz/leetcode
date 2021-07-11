#include <string>

using namespace std;

class Solution {
    std::tuple<int, int> minimum_skip_values = {9999, 9999};
public:
    bool increasingTriplet(vector<int> &nums) {
        for (int i = 0; i < nums.size(); i++) {
            // If the current value is greater than minimum skip value, skip the other process.
            if (nums[i] >= std::get<0>(minimum_skip_values))
                continue;

            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] > nums[i]) {
                    // If the current value is greater than minimum skip value, skip the other process.
                    if (nums[j] >= std::get<1>(minimum_skip_values))
                        continue;

                    for (int k = j + 1; k < nums.size(); k++) {
                        if (nums[k] > nums[j])
                            return true;
                    }
                    std::get<1>(minimum_skip_values) = nums[j];
                }
            }
            std::get<0>(minimum_skip_values) = nums[i];
        }
        return false;
    }
};