first_word = input().upper()
second_word = input().upper()
if first_word < second_word:
    print(-1)
elif first_word > second_word:
    print(1)
else:
    print(0)