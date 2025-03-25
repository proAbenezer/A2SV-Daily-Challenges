# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * len(nums)
        self.prefixSum[0] = nums[0]
        for i in  range(1, len(nums)):
            self.prefixSum[i] = self.prefixSum[i - 1] + nums[i]
        print(self.prefixSum)

    def sumRange(self, left: int, right: int) -> int:
       if left == 0:
        return self.prefixSum[right]
       else:
        return self.prefixSum[right] - self.prefixSum[left - 1]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)