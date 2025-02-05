# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_length = len(nums)
        x_array = nums[:nums_length // 2]
        y_array = nums[nums_length // 2:]
        for n in range(nums_length // 2):
            nums[2* n] = x_array[n]
            nums[2 * n + 1] = y_array[n]
        return nums