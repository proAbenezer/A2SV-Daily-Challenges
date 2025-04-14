# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merged = ""
        p1, p2 = 0, 0 
        n, m = len(word1) , len(word2)
        while p1 < n and p2 < m:
     
            if word1[p1:] < word2[p2:]:
                merged += word2[p2]
                p2 += 1
            else:
                merged += word1[p1]
                p1 += 1

              
        if p1 < n:
            merged += word1[p1:]
        if p2 < m:
            merged += word2[p2:]
  
        return merged
        