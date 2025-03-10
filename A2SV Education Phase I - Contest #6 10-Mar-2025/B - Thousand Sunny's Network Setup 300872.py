# Problem: B - Thousand Sunny's Network Setup - https://codeforces.com/gym/594356/problem/B

n, k = list(map(int, input().split()))
computer = list(map(int, input().split()))

computer.sort(reverse=True)
print(computer[k - 1])
