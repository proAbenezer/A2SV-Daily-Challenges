# Problem: A - The Rules of the Bus - https://codeforces.com/gym/603156/problem/A

t  = int(input())
for c in range(t):
    n = int(input())
    passengers = list(map(int, input().split()))
    seats = [False] * n
    seats[passengers[0] - 1] = True
    res = "YES"
   
    for index, passenger in enumerate(passengers):
        passenger = passenger - 1
        if seats[passenger] == True:
            continue
        elif passenger == 0 and seats[passenger + 1] == False:
            res = "NO"
        elif passenger == n - 1 and seats[passenger - 1] == False:
           
            res = "NO"
        elif seats[passenger - 1] == False and seats[passenger + 1] == False:
                res = "NO"
        
        
        #print(seats)
        seats[passenger] = True


    print(res)



