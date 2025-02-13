# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = {}
        res = []
        for num in nums:
            if num not in seen:
                seen[num] = 1
            elif num in seen:
                seen[num] += 1
                if seen[num] >= 2:
                    res.append(num)
                    del seen[num]
        return res


