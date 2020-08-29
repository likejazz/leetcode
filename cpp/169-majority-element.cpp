class Solution {
public:
    int majorityElement(vector<int> &nums) {
        std::unordered_map<int, int> counter;
        for (int n : nums) {
            counter[n]++;
        }

        for (auto pair : counter) {
            if (pair.second > nums.size() / 2) {
                return pair.first;
            }
        }

        return 0;
    }
};