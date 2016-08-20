import re
def myfindall(regex, seq):
	resultlist=[]
	pos=0
	while True:
	   result = regex.search(seq, pos)
	   if result is None:
	      break
	   resultlist.append(seq[result.start():result.end()])
	   pos = result.start()+1
	return len(resultlist)

hcount = 0
vcount = 0
dcount = 0

m = int(input())
n = int(input())

mArray = []
for i in range(0, m):
	mArray.append(  input().split(' ', n) )
pattern = input()
regex = re.compile(pattern)

#horizontal
for x in mArray:
	if pattern in str(''.join(x)):
		# print(str(''.join(x)))
		hcount = hcount + myfindall(regex, str(''.join(x)))

#vertical
for i in range(0, n):
	tempString = ''
	for j in range(0, m):
		tempString = tempString + mArray[j][i]
	if pattern in tempString:
		vcount = vcount + myfindall(regex, tempString)

#diagonal
if m == n:
	tempString = ''
	for i in range(0, m):
		tempString = tempString + mArray[i][i]

	if pattern in tempString:
			dcount = dcount + myfindall(regex, tempString)

count = str(vcount + hcount + dcount)
print(count)