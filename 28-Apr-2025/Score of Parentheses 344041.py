# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        val, res = 0, 0
        for c in s: 
            if c == "(":
                stack.append(0)
            else: 
                mul = stack.pop()
                if mul == 0:
                    val = 1
                else:
                    val = 2 * mul 

                if not stack: 
                    res += val 
                else: 
                    stack[-1] += val  
        return res