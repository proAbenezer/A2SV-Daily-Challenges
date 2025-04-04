# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
cards = list(map(int, input().split()))

turns = True

sereja = 0
dima  = 0
left, right = 0, n - 1
while left <= right:
    if turns:
        if cards[left] > cards[right]:
            sereja += cards[left]
            left += 1
        else:
            sereja += cards[right]
            right -= 1
        turns = False
    else: 
        if cards[left] > cards[right]:
            dima += cards[left]
            left += 1
        else:
            dima += cards[right]
            right -= 1
        turns = True
print(sereja, dima)