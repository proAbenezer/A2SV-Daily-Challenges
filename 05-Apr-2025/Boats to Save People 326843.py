# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            remain =  limit - people[right]
            boats += 1
            right -= 1
            if people[left] <= remain:
                left += 1
        return boats  
