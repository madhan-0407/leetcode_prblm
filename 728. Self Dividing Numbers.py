from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left,right+1):
            n=[int(x) for x in str(i)]
            print(n)
            if 0 in n:
                continue
            for j in n:
                if i%j!=0:
                    break
            else:
                l.append(i)
        return l



print(Solution().selfDividingNumbers(left=13,right=22))