class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        // nums.count != Set(nums).count
        // time and space complexity = O(n)

        var dict = [Int: Int]()
        for ind in 0..<nums.count {
            if dict[nums[ind]] == nil {
                dict[nums[ind]] = 1
            }else {
                return true
            }
        }
        return false
        }
    // }time and space complexity = O(n)
}