# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for n in nums:
            counts[n] += 1
        
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1