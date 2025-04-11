# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in seen and left <= right:
                seen.remove(s[left])
                left += 1
            res = max(res, right - left + 1)
            seen.add(s[right])
        return res