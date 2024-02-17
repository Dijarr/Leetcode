class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for index, value in enumerate(nums):
            remainder = target - value

            if remainder in visited:
                return [visited[remainder], index]
            
            visited[value] = index 