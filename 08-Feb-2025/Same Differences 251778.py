# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

import sys
from collections import defaultdict

def count_same_differences(test_cases):
    results = []
    
    for n, a in test_cases:
        freq = defaultdict(int)  # Dictionary to store counts of a[i] - i
        count = 0
        
        for i in range(n):
            value = a[i] - i
            count += freq[value]  # Add previous occurrences of the same value
            freq[value] += 1      # Update frequency count
        
        results.append(str(count))
    
    sys.stdout.write("\n".join(results) + "\n")  # Fast output

# Reading input
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # Number of test cases
    index = 1
    test_cases = []
    
    for _ in range(t):
        n = int(data[index])
        a = list(map(int, data[index + 1: index + 1 + n]))
        test_cases.append((n, a))
        index += n + 1
    
    count_same_differences(test_cases)
