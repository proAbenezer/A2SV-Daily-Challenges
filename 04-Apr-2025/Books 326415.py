# Problem: Books - https://codeforces.com/contest/279/problem/B

n, time = list(map(int, input().split()))
books = list(map(int, input().split()))
res = 0 
spentTime = 0
left = 0
for right in range(len(books)):
    spentTime += books[right]
    while spentTime >  time:
        spentTime -= books[left]
        left += 1
    res = max(res, right - left + 1)
print(res)
    
