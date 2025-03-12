# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        size = len(piles)
        numberOfCoins = size / 3
        coins = 0
        p1 = size - 2
        while numberOfCoins > 0:
            coins += piles[p1]
            p1 -= 2
            numberOfCoins -= 1 
        return coins