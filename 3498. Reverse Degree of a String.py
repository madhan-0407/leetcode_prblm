class Solution:
    def reverseDegree(self, s: str) -> int:
        char=[chr(i) for i in range(97,123)]
        rev_num=[i for i in range(26,0,-1)]
        reverse_degree = dict(zip(char,rev_num))
        Product=[]
        for i in range(0,len(s)):
            print(s[i])
            if s[i] in reverse_degree:
                Product.append(reverse_degree[s[i]]*(i+1))
        return sum(Product)


s=Solution()
print(s.reverseDegree(s = "zaza"))

