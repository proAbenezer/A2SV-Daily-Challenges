# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = res = windowSum = 0

        for right in range(len(nums)):
            while nums[right] in seen and left <= right:
                seen.remove(nums[left])
                windowSum -= nums[left]
                left += 1
            seen.add(nums[right])
            windowSum += nums[right]
            res = max(res, windowSum)
        return res 