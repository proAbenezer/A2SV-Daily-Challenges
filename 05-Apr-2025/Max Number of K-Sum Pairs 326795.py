# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum > k:
                right -= 1
            elif sum < k:
                left += 1
            else:
                res += 1
                left += 1
                right -= 1

        return res
        