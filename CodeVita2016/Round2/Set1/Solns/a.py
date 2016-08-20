def lcm(x, y):
    """Returns the least common multiple of x and y."""
    multiples = []
    high = x*y
    for i in range(1,high+1):
        if i % x == 0 and i % y == 0:
            multiples.append(i)
    multiples.sort()
    return multiples[0]

def ParserFunction(inputsStringArray):
	expectedAnswer = 1
	for x in inputsStringArray:
		xArray = x.split()
		if(xArray[0] != 'A'):
			print(xArray[0] + '\'s question is: '+ xArray[1])
			commaSplit = xArray[1].split(',')
			for blah in commaSplit:
				expectedAnswer = lcm(int(expectedAnswer), int(blah))
			# print(expectedAnswer)
		else:
			if(int(xArray[2])%int(expectedAnswer)==0):
				print("Correct Answer")
				print(xArray[1] + ": 10points")
				if(xArray[1]=='Darrell'):
					DarrellScore = DarrellScore + 10




DarrellScore = 0 
SallyScore = 0

Qns = int(input())
inputsStringArray = []

for i in range(0, Qns):
	inputsStringArray.append(input())

ParserFunction(inputsStringArray)

