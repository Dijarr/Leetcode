class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, res, [], 0)
        return res

    def dfs(self, candidates, target, res, cur, index):
        if target == 0 :
            res.append(cur[:])
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                return
            cur.append(candidates[i])
            self.dfs(candidates, target - candidates[i], res, cur, i + 1)
            cur.pop()
        