class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            # we chose the min because the water in the container will spill if we used the max instead of the min
            max_water = max(max_water, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_water