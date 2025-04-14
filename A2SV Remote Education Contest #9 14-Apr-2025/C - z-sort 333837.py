# Problem: C - z-sort - https://codeforces.com/gym/603156/problem/C

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
left, right = 0, n - 1
res = []
turn = True 
while left <= right:
   if turn:
      res.append(nums[left])
      left += 1
   else:
      res.append(nums[right]) 
      right -= 1
   turn = not turn
for num in res:
   print(num, end=" ")