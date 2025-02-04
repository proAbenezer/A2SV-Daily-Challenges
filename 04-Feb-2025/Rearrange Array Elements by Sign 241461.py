# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_integers = []
        negative_integers = []
        for i in range(len(nums)):
            if nums[i] < 0:
                negative_integers.append(nums[i])
            else:
                positive_integers.append(nums[i])
        i = 0
        while 2 * i < len(nums):
            nums[2 * i] = positive_integers[i]
            nums[2 * i + 1] = negative_integers[i]
            i += 1
        return nums

        