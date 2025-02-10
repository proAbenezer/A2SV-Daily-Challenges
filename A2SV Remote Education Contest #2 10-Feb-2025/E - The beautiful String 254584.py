# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

test_cases = int(input())
for test_case in range(test_cases):
    target = list(input().strip())
    length_of_target = len(target)
    numbers_of_queries = int(input())
    count = 0
    for i in range(length_of_target - 3):
        if target[i] == '1' and target[i + 1] == '1' and target[i + 2] == '0' and target[i + 3] == "0":
            count += 1
    
    for queries in range(numbers_of_queries):
        index, value = list(input().split())
        index = int(index) - 1
        if target[index] == value:
            print("YES" if count > 0 else "NO")
            continue 
    
        for i in range(max(0, index - 3), min(index + 1, length_of_target - 3)):
            if target[i] == '1' and target[i + 1] == '1' and target[i + 2] == '0' and target[i + 3] == "0":
                count -= 1

        target[index] = value 

        for i in range(max(0, index - 3), min(index + 1, length_of_target - 3)):
            if target[i] == '1' and target[i + 1] == '1' and target[i + 2] == '0' and target[i + 3] == "0":
                count += 1

        print("YES" if count > 0 else "NO")

 