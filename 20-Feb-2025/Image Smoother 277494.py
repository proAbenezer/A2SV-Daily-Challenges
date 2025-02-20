# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLUMNS = len(img), len(img[0])
        res = [[0] * COLUMNS for _ in range(ROWS)]
        for row in range(ROWS):
            for column in range(COLUMNS):
                total_sum = 0
                count = 0
                for i in range(row - 1, row + 2):
                    for j in range(column - 1, column + 2):
                        if i < 0 or i == ROWS or j < 0 or j == COLUMNS:
                            continue
                        total_sum += img[i][j]
                        count += 1
                res[row][column] = total_sum // count 
        return res