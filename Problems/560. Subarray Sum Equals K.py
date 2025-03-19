from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        dict = defaultdict(int)
        dict[0] = 1
        for n in nums:
            sum += n
            count += dict[sum - k]
            dict[sum] += 1
        return count
