number, clrpattern= input().split()
clrpattern = list(clrpattern)
count  = 0
number = int(number)

for i in range(0, number):
	if ((clrpattern[i] == 'R'  )and (i != number-1)):
		count = count + 1
	elif clrpattern[i] == 'G' and i+1 != number:
		if clrpattern[i+1] == 'R':
			count = count + 1
print(count)