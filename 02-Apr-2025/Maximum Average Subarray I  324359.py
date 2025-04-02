# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        res = window_sum / k
        l = 0 
        for r in range(k, len(nums)):
            window_sum += nums[r]
            window_sum -= nums[l]
            l += 1

            res = max(res, window_sum / k)
        return res
