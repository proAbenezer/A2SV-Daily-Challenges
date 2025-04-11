# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenS = len(s)
        lenP = len(p)
        if lenP > lenS: return []
        sCount = {}
        pCount = {}
        for i in range(lenP):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            pCount[p[i]] = pCount.get(p[i], 0 ) + 1
        res = []
        if sCount == pCount: res.append(0)
        l = 0
        for r in range(lenP, lenS):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res