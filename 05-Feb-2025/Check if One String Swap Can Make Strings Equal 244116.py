# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swaps = 0
        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        if s1_count != s2_count:
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps += 1
        return swaps <= 2
        