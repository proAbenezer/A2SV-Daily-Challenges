# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        index_to_value = {}
        res = [0] * len(nums)
        for index in range(len(nums)):
            index_to_value[index] = nums[index]
        for index in range(len(nums)):
            res[index] = nums[index_to_value[index]]
        return res        