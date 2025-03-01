# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = []
postition= []
for i in range(5):
    row = list(map(int, input().split()))
    for c in range(len(row)):
        if row[c] != 0:
            postition = [i, c]
    matrix.append(row)
print(abs(postition[0] - 3 + 1) + abs(postition[1] - 3 + 1))