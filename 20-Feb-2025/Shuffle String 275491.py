# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = [""] * len(s)
        for c, i in zip(s, indices):
            temp[i] = c
        return "".join(temp)
        