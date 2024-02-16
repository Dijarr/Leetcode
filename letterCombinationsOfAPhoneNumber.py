class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        store = {"2": ['a','b','c'], "3": ['d','e','f'], 
        "4": ['g','h','i'], "5": ['j','k','l'], "6": ['m','n','o'], 
        "7": ['p','q','r','s'], "8": ['t','u','v'], "9": ['w','x','y','z']}
        res = []
        self.dfs(digits, store, res, 0, [])
        return res
            
    def dfs(self, digits, store, res, idx, cur):
        if len(cur) == len(digits):
            res.append("".join(cur))
            return
        
        for char in store[digits[idx]]:
            cur.append(char)
            self.dfs(digits, store, res, idx+1, cur)
            cur.pop()
            