class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        minimal_window = float('inf')
        cur_sum = nums[left]
        while left < n and right < n:
            print(left, right)
            if cur_sum >= target:
                minimal_window = min(minimal_window, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            else:
                right += 1
                if right >= n:
                    break
                cur_sum += nums[right]
        return minimal_window if minimal_window <= 10**9 else 0