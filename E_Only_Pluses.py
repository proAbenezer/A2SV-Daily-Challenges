number_of_testcase = int(input())
for testcase in range(number_of_testcase):
    numbers = list(map(int, input().split()))
    a, b, c = sorted(numbers)
    remaning = 5
    while remaning > 0:
        if a < b:
            a += 1
        elif b < c:
            b += 1
        else:
            c += 1
        remaning -= 1
    print(a * b* c )