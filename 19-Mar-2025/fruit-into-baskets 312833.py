# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        res, total, l = 0, 0, 0
        
        for r in range(len(fruits)):
            total += 1
            count[fruits[r]] += 1
            
            while len(count) > 2:
                f = fruits[l]
                total -= 1
                count[f] -= 1

                if count[f] == 0: count.pop(f)
                l += 1
            res = max(res, total)
        return res