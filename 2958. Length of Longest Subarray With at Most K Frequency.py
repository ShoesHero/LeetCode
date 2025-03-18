from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = {}
        l = 0
        for r in range(len(nums)):
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            if mp[nums[r]] > k:
                while nums[l] != nums[r]:
                    mp[nums[l]] -= 1
                    l += 1
                mp[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans