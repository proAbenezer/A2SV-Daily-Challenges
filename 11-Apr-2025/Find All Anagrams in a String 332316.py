# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenS = len(s)
        lenP = len(p)

        if lenP > lenS: return []

        pCount = {}
        sCount = {}

        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1
        
        res = []

        if pCount == sCount:
            res.append(0)
        left = 0
        for right in range(lenP, lenS):
            sCount[s[right]] = sCount.get(s[right], 0) + 1
            sCount[s[left]] -= 1

            if sCount[s[left]] == 0:
                sCount.pop(s[left])
            left += 1
            if sCount == pCount:
                res.append(left)
        return res

