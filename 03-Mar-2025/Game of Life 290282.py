# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        n, m = len(board), len(board[0])
        placeholder = [[0] * m for _ in range(n)]
        #Going through each row
        for row in range(n):
            #Going through each column
            for column in range(m):

                # The total sum of the elements in the sqaure 
                total_sum = 0

                # The neighboring row
                for i in range(row - 1, row + 2):
                    # The neighboring column
                    for j in range(column - 1, column + 2):
                        #For square with missing elements 
                        if (i < 0 or j < 0) or (i == n or j == m):
                            continue 
                        #calucalting the sum
                        total_sum += board[i][j]
                #substring the original element
                total_sum -= board[row][column]

               
                #checking which rule to apply 
                if total_sum < 2 and board[row][column] == 1:
                    placeholder[row][column] = -1
                elif total_sum == 2 or total_sum == 3 and board[row][column] == 1:
                    placeholder[row][column] = 1
                elif total_sum >= 3 and board[row][column] == 1:
                    placeholder[row][column] = -1
                elif total_sum == 3 and board[row][column] == 0:
                    placeholder[row][column] = 2
        print(placeholder)
        for row in range(n):
            for column in range(m):
                if placeholder[row][column] == -1:
                    board[row][column] = 0
                elif placeholder[row][column] == 2:
                    board[row][column] = 1 
                