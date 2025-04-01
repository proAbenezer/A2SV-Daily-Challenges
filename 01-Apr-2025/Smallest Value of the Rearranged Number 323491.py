# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = sorted(str(abs(num)), reverse= num < 0) # if -ve sort in reverse 
        if digits[0] == '0':
            for i in range(1, len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], '0'
                    break

        return int("".join(digits)) * (1 if num > 0 else -1)