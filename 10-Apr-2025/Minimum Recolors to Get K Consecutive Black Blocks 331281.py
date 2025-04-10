# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    from collections import Counter
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = Counter(blocks[:k])
        res = count["W"]
        if k == len(blocks):
            return count["W"]
            
        for i in range(0, len(blocks) - k):
           count[blocks[i]] -= 1
           count[blocks[i + k]] += 1
           res = min(res, count["W"])
        return 0 if res == float("inf") else res

        