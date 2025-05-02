# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

class Solution:
    def printTillN(self, N):
    	#code here 
    	if N == 0:
    	    return 1
    	print(self.printTillN(N - 1), end=" ")
    	
    	return N + 1