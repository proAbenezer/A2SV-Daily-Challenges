# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        nums1Index = {n:i for i, n in enumerate(nums1)}
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and stack[-1] < cur:
                val = stack.pop()
                index = nums1Index[val] 
                res[index] = cur
            if cur in nums1Index:
                stack.append(cur)
        return res
            