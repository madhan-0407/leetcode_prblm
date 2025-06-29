class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

print(Solution().countSegments(s = "Hello, my name is John"))