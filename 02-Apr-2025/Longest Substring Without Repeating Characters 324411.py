# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        l = 0 
        for r in range(len(s)):
            while s[r] in seen and l <= r:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            seen.add(s[r])
        return res
