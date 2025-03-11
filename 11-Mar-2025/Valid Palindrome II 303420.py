# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalidrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False 
                l += 1
                r -= 1 
            return True
        left, right = 0, len(s) - 1
        while left < right: 
            if s[left] != s[right]:
                return checkPalidrome(left + 1, right) or checkPalidrome(left, right - 1)
            left += 1
            right -= 1
        return True 