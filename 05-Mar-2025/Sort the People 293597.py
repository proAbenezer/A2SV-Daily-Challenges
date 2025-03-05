# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #using bubble sort 
        for i in range(len(heights) - 1, -1, -1):
            for j in range(1, i + 1):
                if heights[j] > heights[j - 1]:
                    heights[j - 1], heights[j] = heights[j], heights[j - 1]
                    names[j - 1], names[j] = names[j], names[j - 1]
        return names