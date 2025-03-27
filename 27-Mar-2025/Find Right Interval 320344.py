# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    from collections import defaultdict
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts, ends = [], []
        startToIndex = defaultdict(int)
        res = []
        for start, end in intervals:
            starts.append(start)
            ends.append(end)
        for index, interval in enumerate(intervals):
            startToIndex[interval[0]] = index
        starts.sort()
        for _, end in intervals:
            idx = bisect_left(starts, end)  # Binary search for smallest start >= end
            
            if idx < len(starts):  # If a valid interval exists
                res.append(startToIndex[starts[idx]])
            else:
                res.append(-1)

                
        return res