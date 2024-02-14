class Solution {
    func sortColors(_ nums: inout [Int]) {
        var l = 0
        var r = (nums.count ) - 1
        var i = 0

        while i <= r {
            if nums[i] == 0 {
                nums.swapAt(i, l)
                l += 1
                i += 1
            } else if nums[i] == 2 {
                nums.swapAt(i, r)
                r -= 1
            } else {
                i += 1
            }
        }
    }
}

    