# 0001
# 0010
# 0011
# 0100
# 0101
# 0110
# 0111
# 1000
# 1001
# 1010
# 1011
# 1100
# 1101
# 1110
# 1111
def bitcount(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n & (n-1)
    return count

def isEven(n):
	if(bitcount(n)==2):
		# print("debugisEven: ", n)
		return 1
	else:
		return 0

def getSum(N):
	sum = 0
	count = 0
	i=3
	while count<N:
		if(isEven(i)==1):
			count =  count + 1
			# print("debug: ", count)
			sum = sum + i
		i = i + 1

	sum = sum %1000000007
	print(str(sum))

args=int(input())
A= []
i=0
while i<args:
	A.append(input())
	i = i + 1
for val in A:
	getSum(int(val))
