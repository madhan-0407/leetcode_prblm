from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==len(list(set(nums))):
            return True
        else:
            return False

print(Solution().containsDuplicate(nums = [1,2,3,1]))