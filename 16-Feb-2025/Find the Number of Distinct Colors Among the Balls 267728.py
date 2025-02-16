# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        from collections import Counter
        distincitBalls = Counter() # color -> count
        ballsToColor = defaultdict() # ball -> color

        result = []
        for ball, color in queries:

            distincitBalls[color] += 1

            if ball in ballsToColor:
                old_color = ballsToColor[ball]
                distincitBalls[old_color] -= 1


                if distincitBalls[old_color] == 0:
                    distincitBalls.pop(old_color)
            ballsToColor[ball] = color

            result.append(len(distincitBalls))
        return result