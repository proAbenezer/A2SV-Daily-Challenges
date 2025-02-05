# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        current_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_max += 1
                max_length = max(max_length, current_max)
            else:
                current_max = 0
        return max_length
        