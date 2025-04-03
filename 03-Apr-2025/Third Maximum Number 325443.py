# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    from collections import Counter
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        if len(nums) < 3: return max(nums)
        return nums[2]