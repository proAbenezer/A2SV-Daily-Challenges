# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

def findGeometricSum(n): 
    if n == 0:
        return 1 
    

    res = findGeometricSum(n - 1)

    return 1 / (3 ** n)

print(findGeometricSum(5))
