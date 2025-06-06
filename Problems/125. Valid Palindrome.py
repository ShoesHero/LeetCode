import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^A-Za-z0-9]", "", s)
        s = s.lower()

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True