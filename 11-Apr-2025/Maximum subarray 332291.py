# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currentSum = 0
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            res = max(res, currentSum)
        return res
