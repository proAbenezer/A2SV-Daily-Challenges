# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 0
        if len(s) <= 1:
            return 1
        for i in range(len(s)):
            count = 0
            for j in range(i + 1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                if count > 1:
                    break
                res = max(res, j - i + 1)
        return res
