# Problem: B - Ski Resort - https://codeforces.com/gym/603156/problem/B

t = int(input())

for _ in range(t):
    n, k, q = list(map(int, input().split()))
    temp = list(map(int, input().split()))

    res = 0
    i = 0
    while i < n:
     
        if temp[i] > q:
            i += 1
            continue
        j = i
        while j < n and temp[j] <= q:
            #print(i, j)
            j += 1
        days = j - i
        if days >= k:
            count = (days - k + 1) * (days - k + 2) // 2
            res += count 
        #print(days, consectiveDays, res)

        
        i = j
    print(res)
        