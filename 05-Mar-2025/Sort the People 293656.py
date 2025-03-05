# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #using bubble sort 
        size = len(heights)
        swapped = True 
        for i in range(size):
            swapped = False 
            for j in range(size - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
                    swapped = True
            if not swapped:
                break
        return names
