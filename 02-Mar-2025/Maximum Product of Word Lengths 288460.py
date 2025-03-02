# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = [[0] * 26 for _ in range(len(words))]
        longest_product = 0
        def compare(word1, word2):
            for c1, c2 in zip(word1, word2):
                if c1 != 0 and c2 != 0:
                    return True
            return False
        for i in range(len(words)):
            for char in words[i]:
                res[i][ord(char) - ord("a")] += 1
       
        for i in range(len(words) - 1): 
            for j in range(i + 1, len(words)):
               if  not compare(res[i], res[j]):
                    longest_product = max(longest_product, sum(res[i]) * sum(res[j]))
        return longest_product
 