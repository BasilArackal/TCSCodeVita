def palindrome(blah):
	if blah == blah[::-1]:
		return True
	else:
		return False

pd  = input().split(',')
palList = []
for i in range(int(pd[0]), int(pd[1])+1):
	if palindrome(str(i)):
		palList.append(i)
print(palList)
allowedList = []
for i in range(0, len(palList)):
	if(palList[i+1]-palList[i] < pd[2]):
		allowedList.append(palList)