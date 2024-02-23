class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = {}
        for char in magazine:
            check[char] = check.get(char, 0) + 1
        for char in ransomNote:
            if char not in check:
                return False
            else:
                check[char] = check.get(char) - 1
                if check[char] == 0:
                    check.pop(char)
        return True
# time and space complexity = O(m+n), O(m)     