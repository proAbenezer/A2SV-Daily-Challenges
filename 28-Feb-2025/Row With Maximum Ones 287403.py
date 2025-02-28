# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result = [0, 0]
        for i, row in enumerate(mat):

            ones_count = row.count(1)
          
            if result[1] < ones_count:
                result = [i, ones_count]   
        return result 
        