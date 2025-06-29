class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if len(str(num**0.5))>10:
            return False
        else:
            return True

print(Solution().isPerfectSquare(num=5))