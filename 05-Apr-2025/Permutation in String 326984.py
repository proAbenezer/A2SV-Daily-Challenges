# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        lenS2 = len(s2)
        
        if lenS1 > lenS2: return []
        s1Count, s2Count = {}, {}
        
        for i in range(lenS1):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0 ) + 1
        if s1Count == s2Count: return True

        l = 0
        for r in range(lenS1, lenS2):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1
            s2Count[s2[l]] -= 1

            if s2Count[s2[l]] == 0:
                s2Count.pop(s2[l])
            l += 1
            if s1Count == s2Count:
                return True
        return False