# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def convertString(strs, n):
    if n == len(strs) - 1:
        return int(strs[-1])   


    res = convertString(strs, n + 1)

    return res + (int(strs[n]) * 10 ** (len(strs) - n - 1))
