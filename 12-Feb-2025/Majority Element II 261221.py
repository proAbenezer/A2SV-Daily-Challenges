# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        majorityElement = len(nums) // 3
        res = []
        counts = Counter(nums)
        for count in counts:
            if counts[count] > majorityElement:
                res.append(count)
        return res
        