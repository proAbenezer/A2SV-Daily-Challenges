# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 0
        if len(s) == 1:
            return 1
        
        left = 0
        count = 0
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                count += 1
            while count > 1:
                left += 1
                if s[left] == s[left - 1]:
                    count -= 1
            res = max(res, right - left + 1)
        return res