# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
       seen = {}
       res = []
       for num in nums:
        if num in seen:
            res.append(num)
            seen.pop(num)
        else:
            seen[num] = 1    

       return res    