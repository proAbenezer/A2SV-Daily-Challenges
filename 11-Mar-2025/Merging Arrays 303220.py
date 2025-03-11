# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

p1, p2 = 0, 0
res = []
while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] <= arr2[p2]:
        res.append(arr1[p1])
        p1 += 1
    else:
        res.append(arr2[p2])
        p2 += 1
if p1 != len(arr1):
    res.extend(arr1[p1:])
else:
    res.extend(arr2[p2:])
for i in range(len(res)):
    print(res[i], end=" ")