# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

n, t = list(map(int, input().split()))
min_num = 10 ** (n - 1)
    
if min_num % t == 0:
    result = min_num
else:
    result = (min_num // t + 1) * t

if result < 10 ** n:
    print(result)
else:
    print(-1)