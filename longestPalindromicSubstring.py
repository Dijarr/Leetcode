class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength = 0
        result = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                cand = s[i:j]
                if cand == cand[::-1] and len(cand) > maxlength:
                    maxlength = len(cand)
                    result = cand
        return result
            