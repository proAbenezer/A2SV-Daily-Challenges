# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Base case: If there is only one person, they are the winner.
        if n == 1:
            return 1
      
        # Recursive call to find the winner among (n-1) people.
        # The winner's position among n people is offset by k positions from 
        # the position among (n-1) people.
        winner = (k + self.findTheWinner(n - 1, k)) % n
      
        # If modulo operation results in 0, the winner is at the nth position
        # because indexing starts from 1, not 0.
        # Otherwise, return the calculated winner position.
        return n if winner == 0 else winner


       

