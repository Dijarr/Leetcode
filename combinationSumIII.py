class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(1, [], k, n, res)
        return res

    def dfs(self, num, cur, k, n, res):
        if len(cur) == k and sum(cur) == n:
            res.append(cur[:])
        if sum(cur) > n or k > n:
            return
        for i in range(num, 10):
            cur.append(i)
            self.dfs(i + 1, cur, k, n, res)
            cur.pop()
        