# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i in range(len(nums)):
            if stack and nums[i] < nums[stack[-1]]:
                stack.append(i)
        res = 0 
        for r in range(len(nums) -  1, -1, -1):
            while stack and nums[stack[-1]] <= nums[r]:
                l = stack.pop()
                res = max(res, r - l)
        return res