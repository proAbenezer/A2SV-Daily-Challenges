# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_count = {}
        for i in range(len(nums)):
            nums_count[nums[i]]  = nums_count.get(nums[i], 0) + 1
        pair_count = 0
        leftover_count = 0

        for count in nums_count:
            if nums_count[count] % 2 != 0:
                leftover = nums_count[count] % 2
                leftover_count += leftover
                pair_count += (nums_count[count] - leftover) // 2
            else:
                pair_count += nums_count[count] // 2
        return [pair_count, leftover_count]