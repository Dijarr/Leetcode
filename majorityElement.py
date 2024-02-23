class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    #     nums.sort()
    #     n = len(nums)
    #     mid = n // 2
    #     return nums[mid]
    # time complexity: O(n log n)

        dic = {}
        n = len(nums)
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        mid = n // 2
        for key, value in dic.items():
            if value > mid:
                return key
        return 0
    # time and space complexity: O(n), O(n)