# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    from collections import defaultdict
    def longestSquareStreak(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxStreak = -1
        for num in nums:
            streak = 0
            while num in numsSet:
                num *= num
                streak += 1
            if streak > 1:
                maxStreak = max(maxStreak, streak)
        return maxStreak