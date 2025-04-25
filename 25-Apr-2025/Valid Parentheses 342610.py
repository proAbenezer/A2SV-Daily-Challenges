# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s: 
            if c in closedToOpen:
                if stack and closedToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return True 