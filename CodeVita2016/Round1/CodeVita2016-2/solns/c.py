def funk(mom):
	totSweets = 0
	for no in mom:
		totSweets = totSweets + int(no)
	return totSweets

def countThree(mom):
	count = 0
	for no in mom:
		if(int(no)%3==0):
			count = count + 1
	return count+1

n = int(input())
mom = input().split()

if(funk(mom)%3==0):
	print("Yes " + str(countThree(mom)))
else:
	print("No")
