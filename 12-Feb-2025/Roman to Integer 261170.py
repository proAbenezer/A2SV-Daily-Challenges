# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInteger = {"I":1,"V":5,"X":10,"L":50,"C":100,"D": 500,"M":1000}
        pattern = {"IV": 2,"IX": 2 ,"XL": 20, "XC": 20, "CD": 200, "CM": 200}
        res = 0
        count = 0
        for p in pattern:
            if p in s:
                count -= pattern[p] 
                print(p)
        s = list(s)
        for c in s:
            res += romanToInteger[c]
        

        return res + count
            