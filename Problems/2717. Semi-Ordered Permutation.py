from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        min = nums.index(1)
        max = nums.index(len(nums))

        if min > max:
            return min + len(nums) - max - 2
        else:
            return min + len(nums) - max - 1