# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        res = []
        for i in range(n):
            if arr[i] == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(arr[i])
        arr.clear()
        arr.extend(res[:n])
        print(arr)
