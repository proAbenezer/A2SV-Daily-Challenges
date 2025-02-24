# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

from collections import deque
numberOfMessage = int(input())
seen = {}
message = []
for index in range(numberOfMessage):
    name = input()
    if name in seen:
        message[seen[name]] = 0
    message.append(name)
    seen[name] = index

for index in range(len(message) - 1, -1, -1):
    if message[index] != 0:
        print(message[index])