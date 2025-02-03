def sortSentence(s):
    res  = ""
    list_of_strings = list(s.split())
    list_of_strings.sort(key=lambda word: word[-1])
    for word in list_of_strings:
        res = res + " " + word[:len(word) - 1]
    return res.strip()
print(sortSentence("is2 sentence4 This1 a3"))