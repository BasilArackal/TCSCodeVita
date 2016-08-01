import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

N, K = input().split()
N= int(N)
K = int(K)
res = 0
for k in range(0, K+1, 2):
	res = res + int(nCr(N,k))
print( str(res) )
