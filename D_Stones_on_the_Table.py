number_of_stones = int(input())
stones = input()
res = number_of_stones
for i in range(1, number_of_stones):
    if stones[i] == stones[i - 1]:
        res -= 1
print(number_of_stones - res)