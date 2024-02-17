class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                cur_sum = nums[i] + nums[r] + nums[l]
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum < target:
                    l += 1
                else:
                    r -= 1

        return res
        