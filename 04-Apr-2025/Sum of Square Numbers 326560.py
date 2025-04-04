# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squareRoot = set()
        for i in range(int(sqrt(c)) + 1):
            squareRoot.add(i * i)
        a = 0
        while a * a <= c:
            target = c - a * a 
            if target in squareRoot:
                return True
            a += 1
        return False