# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answerCount = Counter(answers)
        res = 0

        for answer, count in answerCount.items():
            group = math.ceil((count / (answer + 1)))
            res += group * (answer + 1)
        return res

