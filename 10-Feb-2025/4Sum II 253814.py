# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        pairwise_sum_count = {}
        for n1 in nums1:
            for n2 in nums2:
                target = n1 + n2 
                pairwise_sum_count[target] = pairwise_sum_count.get(target, 0) + 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                target = -(n3 + n4)
                if target in pairwise_sum_count:
                    count += pairwise_sum_count[target]
        return count
