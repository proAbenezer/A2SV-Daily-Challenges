# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        l = 0
        total_sum = 0  
        for r in range(len(nums)):
            total_sum += nums[r]
            while total_sum >= target and l <= r:
                res = min(res, r - l + 1)
                total_sum -= nums[l]
                l += 1
        return 0 if res == float("inf") else res