N=input()
N = int(N)
A = []
for i in range(0, N+1):
	A.append(i)
#print(A)
for p in range(2, N+1):
	if(p*p > N):
		break
	if A[p] !=  0 :
		for i in range(p*2, N+1, p):
			A[i]=0
sum = 5
count = 0
for j in range(5, N+1, 2):
	if( (A[j] !=0 and A[j] == sum) or A[j] ==  -1):
		count = count + 1
	if( (A[j] !=0 or A[j] == -1)):
		sum = sum + j
	try:
		if( A[sum] != 0 ):
		 	A[sum] = -1
	except IndexError:
		pass
print(str(count))		
# print(A)
