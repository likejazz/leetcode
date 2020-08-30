#include <iostream>
#include <unordered_map>
#include <vector>
#include <sstream>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    string mostCommonWord(string paragraph, vector<string> &banned) {
        std::unordered_map m = unordered_map<string, int>();

        // Transform non-alphanumeric to space.
        std::transform(paragraph.begin(), paragraph.end(), paragraph.begin(),
                       [](unsigned char c) {
                           if (std::isalnum(c)) {
                               return std::tolower(c);
                           } else {
                               return 32;
                           }
                       });

        // Split std::string into std::vector<string> with space delimiter.
        istringstream iss(paragraph);
        vector<string> tokens;
        copy(istream_iterator<string>(iss),
             istream_iterator<string>(),
             back_inserter(tokens));

        for (string token : tokens) {
            if (std::find(banned.begin(), banned.end(), token) == banned.end()) {
                m[token]++;
            }
        }

        // Find the key of the max element.
        unsigned currentMax = 0;
        std::string arg_max;
        for (auto it = m.cbegin(); it != m.cend(); ++it) {
            if (it->second > currentMax) {
                arg_max = it->first;
                currentMax = it->second;
            }
        }

        return arg_max;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

// 819

int main(int argc, const char *argv[]) {
    string paragraph = "a, a, a, a, b,b,b,c, c";
    vector<string> banned;
    banned.push_back("a");

    Solution s = Solution();
    string r = s.mostCommonWord(paragraph, banned);

    cout << r << endl;

    return 0;
}
