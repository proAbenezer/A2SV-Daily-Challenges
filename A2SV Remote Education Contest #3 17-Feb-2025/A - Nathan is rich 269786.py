# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

number_of_testcases = int(input())
for testcase in range(number_of_testcases):
    wheels = int(input())
    min_vehicles = 0
    if wheels == 2:
        min_vehicles = 1
    else:
        min_vehicles += wheels // 4
        if wheels % 4 == 2:
            min_vehicles += 1
    
    print(min_vehicles)