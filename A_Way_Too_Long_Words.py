number_of_testcases = int(input())
for _ in range(number_of_testcases):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)