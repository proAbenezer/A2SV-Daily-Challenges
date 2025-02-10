# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B

test_cases = int(input())
for test_case in range(test_cases):
    length_of_cells = int(input())
    cells = input()
    left, right = 0, length_of_cells - 1
    min_length= 1
    while left < length_of_cells:
        if cells[left] == "B":
            break
        left += 1
    while right > 0:
        if cells[right] == "B":
            break
        right -= 1
    min_length = right - left + 1
    print(min_length)