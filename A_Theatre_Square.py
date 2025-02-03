n, m, a = list(map(int, input().split()))
n = n // a + (n % a != 0)
m = m // a + (m % a != 0)
print(n * m)