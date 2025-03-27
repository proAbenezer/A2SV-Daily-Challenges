# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    from collections import defaultdict
    def relativeSortArray(self, n: List[int], m: List[int]) -> List[int]:
        nCount = [0] * (max(n) + 1)
        mMap = set(m)
        end = []
        result = []
     
        for index, num in enumerate(n):
            if num not in mMap:
                end.append(num)
            nCount[num] += 1
        for index, num in enumerate(m):
            for _ in range(nCount[num]):
                result.append(num)
        end.sort()
        return result + end 