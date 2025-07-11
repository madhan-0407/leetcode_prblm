from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==1:
            return float(nums1[len(nums1)//2])
        else:
            return (nums1[len(nums1)//2-1] + nums1[len(nums1)//2])/2

print(Solution().findMedianSortedArrays(nums1 = [1,3,4], nums2 = [2]))