# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]