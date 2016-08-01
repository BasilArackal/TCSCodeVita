def magic(ro):
	myRow = ""
	for i in range(0, len(ro)):
		if(i%2==0):
			myRow = myRow + ((ord(ro[i])-64)*'0')
		else:
			myRow = myRow + ((ord(ro[i])-64)*'!')
	print(myRow)
asciistringArray = input().split()
for ro in asciistringArray:
	magic(ro)