# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total_sum = 0
        res = [0] * len(queries)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                total_sum += nums[i]

        for i in range(len(queries)):
            value, index = queries[i]
            if nums[index] % 2 == 0:
                total_sum -= nums[index]

            nums[index] += value

            if nums[index] % 2 == 0:
                total_sum += nums[index]

            res[i] = total_sum 

        return res
