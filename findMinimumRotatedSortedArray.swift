class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var res = Int.max, l = 0, r = nums.count - 1
        
        while l <= r{
            if nums[r] > nums[l]{
                res = min(res, nums[l])
            }

            let mid = (l + r) / 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]{
                l = mid + 1
            } else {
                r = mid - 1
            }
        }
        return res
    }
}