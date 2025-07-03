from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l1=list(set(nums))
        n=0
        for i in l1:
            if nums.count(i)>n:
                n=nums.count(i)
                m=i
        return m

print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))