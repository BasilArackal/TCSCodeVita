def findNthNo(n):
	x=0
	y=6
	if(n==1):
		return str(6).zfill(5)
	else:
		for i in range(0, n-1):
			z= abs(x-16-2*y)
			x=y
			y=z
		return str(z).zfill(5)

val = int(input())
if (val>0 or val<=14):
	shit = 1
	for j in range(1,val+1):
		for k in range(j, 0, -1):
			print(findNthNo(shit), end=" ")
			shit = shit + 1
		print()

