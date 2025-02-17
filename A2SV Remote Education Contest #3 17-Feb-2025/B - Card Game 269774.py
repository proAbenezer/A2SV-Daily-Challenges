# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B


n = int(input())
cards =  [int(num) for num in input().split()]
tuple_cards = [(cards[i], i) for i in range(n)]
tuple_cards.sort()
right = n - 1

for left in range(n // 2):
    print(tuple_cards[left][1] + 1, tuple_cards[right][1] + 1)

    right -= 1