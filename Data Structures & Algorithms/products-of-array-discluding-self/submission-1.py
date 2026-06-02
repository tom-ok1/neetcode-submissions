
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        to_right = [0] * len(nums)
        to_right[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            to_right[i] = to_right[i + 1] * nums[i]
        to_left = [0] * len(nums)
        to_left[0] = nums[0]
        for i in range(1, len(nums)):
            to_left[i] = to_left[i - 1] * nums[i]

        ans = []
        for i in range(len(nums)):
            left = to_left[i - 1] if i > 0 else 1
            right = to_right[i + 1] if i < len(nums) - 1 else 1
            ans.append(left * right)
        return ans