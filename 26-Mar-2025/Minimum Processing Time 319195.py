# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    from itertools import cycle
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        maxValues = []
        for i in range(0, len(tasks), 4):
            maxValues.append(max(tasks[i:i + 4]))
        res = 0
        maxValues.sort(reverse=True)
        for task, value in zip(maxValues, cycle(processorTime)):
            res = max(res, task + value)
        return res
             