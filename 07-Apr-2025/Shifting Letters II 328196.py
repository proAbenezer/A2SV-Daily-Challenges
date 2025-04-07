# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefixSums = [0] * (n + 1)
        for start, end, direction in shifts:
            d = 1
            if direction == 0:
                d = -1
            prefixSums[start] += d
            prefixSums[end + 1] -= d

        for i in range(1, n):
            prefixSums[i] = prefixSums[i] + prefixSums[i - 1]
        print(prefixSums)

        res = []
        for i in range(n):
            shift = (ord(s[i]) - ord("a") + prefixSums[i]) % 26
            res.append(chr(shift + ord("a")))
        return "".join(res)
