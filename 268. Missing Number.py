from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                return i
        else:
            return len(nums)

print(Solution().missingNumber(nums=[0,1]))