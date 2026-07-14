class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1, 0, -1):
            diff = target - nums[i]
            if nums.count(diff) > 0:
                return [nums.index(diff), i]        