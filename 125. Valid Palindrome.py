class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string=[]
        for i in s:
            if i.isalnum():
                new_string.append(i.lower())
        new_string=''.join(new_string)
        return new_string==new_string[::-1]


print(Solution().isPalindrome(s ="0P"))