class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var res = [[Int]]()
        dfs(&res, candidates, target, 0, [])
        return res
    }
    
    func dfs(_ res: inout [[Int]], _ candidates: [Int], _ target: Int, _ index: Int, _ curSum: [Int]) {
        if curSum.reduce(0, +) > target {
            return
        }
        if curSum.reduce(0, +) == target {
            res.append(curSum)
            return
        }

        for i in index..<candidates.count {
            var newSum = curSum
            newSum.append(candidates[i])
            dfs(&res, candidates, target, i, newSum)
        }
    }
}
