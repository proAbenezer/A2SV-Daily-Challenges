number_of_testcases = int(input())
res = 0
for testcases in range(number_of_testcases):
    numbers = list(map(int, input().split()))
    res += 1 if sum(numbers) >= 2 else 0
print(res)