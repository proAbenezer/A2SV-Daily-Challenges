# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        intNum = []
        for num in nums:
            intNum.append(int(num))
        intNum.sort(reverse=True)
        return str(intNum[k - 1])
        