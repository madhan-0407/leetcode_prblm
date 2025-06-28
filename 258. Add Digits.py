class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        num=[int(i) for i in num]
        while True:
            num = sum(num)
            if num < 10 and num >= 0:
                return num
            else:
                return self.addDigits(num)

print(Solution().addDigits(num=0))