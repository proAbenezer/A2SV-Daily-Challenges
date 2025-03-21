# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums = sorted(nums, key = lambda num: num[0])
        output = [nums[0]]
        for start, end in nums[1:]:
            lastEnd = output[-1][1]
            if lastEnd >= start:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output