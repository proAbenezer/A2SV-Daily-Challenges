# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        longestSequence = 0
        p1, p2 = 0, 0
        while p1 < len(t) and p2 < len(s):
            if t[p1] == s[p2]:
                p1 += 1
                longestSequence = max(longestSequence, p1)
            p2 += 1

        return len(t) - longestSequence
