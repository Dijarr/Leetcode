class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var max_water = 0
        var l = 0
        var r = height.count - 1

        while l < r{
            var area = (r - l) * min(height[l], height[r])
            max_water = max(max_water, area)
            if height[l] > height[r]{
                r -= 1
            } else {
                l += 1
            }
        }
        return max_water
        
    }
}
// time and space complexity = O(n), O(1)