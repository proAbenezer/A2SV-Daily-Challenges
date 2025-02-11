# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        from collections import defaultdict
        value_to_index = defaultdict(int)
        for index, value in enumerate(nums):
            value_to_index[value] = index
        for oldValue, newValue in operations:
            index = value_to_index[oldValue]
            nums[index] = newValue
            value_to_index.pop(oldValue)
            value_to_index[newValue] = index
        return nums
        