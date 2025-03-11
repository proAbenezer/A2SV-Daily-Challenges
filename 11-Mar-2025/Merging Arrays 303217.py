# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

def mergArray(m, n, a, b):
    p1 =  p2 = 0
    mergedArray = list()
    while p1 < m and p2 < n:
        if a[p1] < b[p2]:
            mergedArray.append(a[p1])
            p1 += 1
        elif  b[p2] < a[p1]:
            mergedArray.append(b[p2])
            p2 += 1
        else:
            mergedArray.append(a[p1])
            mergedArray.append(b[p2])
            p1 += 1
            p2 += 1
    mergedArray.extend(a[p1:])
    mergedArray.extend(b[p2:])
    return mergedArray

m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


mergedArray = mergArray(m, n, a, b)
print(*mergedArray)
"""
6 7
1 6 9 13 18 18
2 3 8 13 15 21 25
"""