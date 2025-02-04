# Problem: Presents - https://codeforces.com/problemset/problem/136/A

number_of_friends = int(input())
gift_list = list(map(int, input().split()))
reciver_to_giver = []
for index in range(len(gift_list)):
    reciver_to_giver.append([index + 1, gift_list[index]])
reciver_to_giver.sort(key=lambda x: x[1])
for gavers in reciver_to_giver:
    print(str(gavers[0]), end=" ") 

