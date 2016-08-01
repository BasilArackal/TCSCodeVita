def isPrime(num):
	meh = 0
	if num > 1:
	   for i in range(2,num):
	       if (num % i) == 0:
	           break
	   else:
	       meh = 1
	else:
	   pass
	return meh

def checkWithi(a, i):
	allPass = 1
	p=a 
	for y in range(0, i):
		pf=2*p+1
		p=pf
		if(isPrime(pf)==0):
			allPass = 0
			break
	if(allPass==1):
		return a
	else:
		return -1
		
def isValid(N, i):
	for x in range(0, N):
		if(isPrime(x)==1):
			if(checkWithi(x, i)>0):
				print(str(checkWithi(x, i)), end=" ")
N = int(input())
I = int(input())
isValid(N, I)
# print()