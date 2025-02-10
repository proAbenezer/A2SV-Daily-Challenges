# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

length_of_word = int(input())
word = input()

result = []
for char in reversed(word):
    l = len(result) + 1
    if l % 2 == 1:
        pos = (l - 1) // 2
    else:
        pos = (l//2) - 1
    result.insert(pos, char)
print("".join(result))