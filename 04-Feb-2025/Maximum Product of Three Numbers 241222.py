# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        product_left = nums[-1] * nums[-2] * nums[-3]
        product_right = nums[0] * nums[1] * nums[-1]
        return max(product_left, product_right)