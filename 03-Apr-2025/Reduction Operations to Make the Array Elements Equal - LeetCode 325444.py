# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res = 0
        count = 0
        nums.sort()
        for index, value in enumerate(nums[1:]):  
            if value != nums[index]:
                count += 1
            res += count
        return res