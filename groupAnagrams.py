class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = " ".join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        res = []
        for value in anagrams.values():
            res.append(value)
        return res
# time = O(n * k log k) where "n" is the total number of strings in strs and "k" is the maximum lenght of a string.
# space complexity = O(n*k) where "n" is the total number of keys in the anagram and "k" is the lenght of a string in strs 