class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        forward = 1
        for i in range(len(nums)):
            output[i] = forward
            forward *= nums[i]

        backward = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= backward
            backward *= nums[i]

        return output