# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    from collections import deque
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        i = 0 
        n = len(tickets)
        while tickets[k] != 0:
            if tickets[i] == 0:
                i = (i + 1) % n
                continue
            tickets[i] -= 1
            i = (i + 1) % n
            seconds += 1
        return seconds