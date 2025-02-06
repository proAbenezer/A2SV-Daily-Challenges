# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a, b, c = [], [], []
        for num in nums:
            if num > pivot:
                c.append(num)
            elif num < pivot:
                a.append(num)
            else:
                b.append(num)
        
        return a + b + c






