# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def findGeometricSum(n): 
    if n == 1:
        return "1" 
    

    res = findGeometricSum(n // 2)

    return res + "1" if n % 2 == 1 else "0"
print(findGeometricSum(7))