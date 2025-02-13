# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        res = []
        nums_count = Counter(nums)
        for num in nums_count:
            if nums_count[num] >= 2:
                res.append(num)
        return res