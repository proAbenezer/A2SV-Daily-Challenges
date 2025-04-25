# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        digits = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        for c in s:
            if stack and c in digits:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)