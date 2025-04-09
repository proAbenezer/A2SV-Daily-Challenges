# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p1, p2 = len(trainers) - 1, len(players) - 1
        res = 0
        while p1 >= 0 and p2 >= 0:
            while p2 >= 0 and trainers[p1] < players[p2]:
                p2 -= 1
            if p2 < 0:
                return res
            res += 1
            p1 -= 1
            p2 -= 1
        return res
