class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiou"
        s=list(s)
        l=list()
        for i in range(len(s)):
            if s[i].lower() in vowels:
                l.append(s[i])
                s[i]=0
        for i in range(len(s)):
            if s[i]==0:
                s[i]=l[-1]
                l.pop()

        return ''.join(s)

print(Solution().reverseVowels(s = "IceCreAm"))
