# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
       return [[matrix[column][row] for column in range(len(matrix))] for row in range(len(matrix[0]))]
      