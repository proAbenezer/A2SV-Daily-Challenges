# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

number_of_testcases = int(input())
from collections import defaultdict
for _ in range(number_of_testcases):
    n, k = input().split()
    n = int(n)
    k = int(k)

    zombiesHealth = list(map(int, input().split()))
    zombiesPosition = list(map(int, input().split()))
    newZombiesPosition = defaultdict(int)
    
    for i in range(n):
        newZombiesPosition[abs(zombiesPosition[i])] += zombiesHealth[i]
    
    isAlive = True
    caryyOnBullets = 0

    for i in range(1, n + 1):
        caryyOnBullets += k - newZombiesPosition[i]
        

        if caryyOnBullets < 0:
            isAlive = False
            break
    if isAlive:
        print("YES")
    else:
        print("NO")
# position doesn't matter place them in the same direction
# we don't care if two zombies are in the same cells 
# we don't care is approaching weather the zombie or the player 
# we don't care if a zombie is in front of us we just shoot
