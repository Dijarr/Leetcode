class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[l] = nums[x]
                l += 1
        return l