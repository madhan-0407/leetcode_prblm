from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        print(nums)
        if len(nums)>=3:
            return nums[-3]
        elif len(nums)>=2:
            return nums[-1]
        else:
            return nums[-1]
print(Solution().thirdMax(nums = [-1,2,3]))