//
// Created by Percival on 2025/3/18.
//
#include <string>

class Solution {
public:
    int lengthOfLastWord(std::string s) {
        int ans = 0;
        bool counting = false;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                if (counting)
                    break;
            } else {
                ans++;
                counting = true;
            }
        }
        return ans;
    }
};
