# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    from collections import Counter
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs_count = 0 
        
        for point in points:
            group_count = Counter()

            for p in points:
                distance = (point[0] - p[0]) ** 2 + (point[1] - p[1]) ** 2
                group_count[distance] += 1 
            boomerangs_count += sum(val * (val - 1) for val in group_count.values())
        return boomerangs_count