from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        result = []
        toBeAdded = ''
        buffer = ''
        toBeAdded += str(nums[0])
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                buffer = '->' + str(nums[i])
            else:
                result.append(toBeAdded+buffer)
                toBeAdded = str(nums[i])
                buffer = ''

        if buffer or toBeAdded:
            result.append(toBeAdded + buffer)

        return result