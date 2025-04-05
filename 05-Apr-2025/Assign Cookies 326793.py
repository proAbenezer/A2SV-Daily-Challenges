# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie_index = 0
        for child_index, greed in enumerate(g):
            while cookie_index < len(s) and s[cookie_index] < greed:
                cookie_index += 1

            if cookie_index >= len(s):
                return child_index
            
            cookie_index += 1
        return len(g)