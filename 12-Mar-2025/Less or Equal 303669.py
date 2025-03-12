# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()
if nums[k] == nums[k - 1]:
    print(-1)
else:
    answer = nums[k - 1] + 1
    print(answer)