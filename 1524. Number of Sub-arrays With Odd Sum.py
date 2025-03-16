from collections import defaultdict
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        track = [1,0]
        sum = 0
        ans = 0
        for n in arr:
            sum = (sum + n) % 2
            if sum:
                ans += track[0]
            else:
                ans += track[1]
            track[sum] += 1
        return ans % (10**9+7)
