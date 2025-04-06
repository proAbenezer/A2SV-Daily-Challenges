# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    from collections import defaultdict

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderToIndex = {0: -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            remainder = total % k
            if remainder not in remainderToIndex:
                remainderToIndex[remainder] = i
            elif i - remainderToIndex[remainder] > 1:
                return True
        return False
