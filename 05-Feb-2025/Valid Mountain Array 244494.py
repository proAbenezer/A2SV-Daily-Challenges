# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
       arr_length = len(arr)
    
       if arr_length < 3:
        return False
       left_pointer, right_pointer = 0, arr_length - 1
       while left_pointer + 1 < arr_length - 1 and arr[left_pointer] < arr[left_pointer + 1]:
        left_pointer += 1
       while right_pointer - 1 > 0 and arr[right_pointer] < arr[right_pointer - 1]:
        right_pointer -= 1
       return left_pointer == right_pointer