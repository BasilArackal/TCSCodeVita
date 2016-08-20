
# DarrellScore = 0 
# SallyScore = 0

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
	DarrellScore = 0 
	SallyScore = 0
	InvalidAno = 0
	expectedAnswer = 1
	for x in inputsStringArray:
		xArray = x.split()
		xArrayLength = len(xArray)
		
		if(xArray[0] != 'A'):
			if(xArrayLength<2):
				print('Invalid Input')
				InvalidAno = 1
				break
			print(xArray[0] + '\'s question is: '+ xArray[1])
			commaSplit = xArray[1].split(',')
			for blah in commaSplit:
				expectedAnswer = lcm(int(expectedAnswer), int(blah))
			# print(expectedAnswer)
		elif xArray[0] == 'A':
			if(xArray[2]== 'PASS'):
				print('Question is PASSed')
				print('Answer is: ' + str(expectedAnswer))
				print(xArray[1] + ": 0points")
			elif(int(xArray[2])%int(expectedAnswer)==0):
				print("Correct Answer")
				expectedAnswer = 1
				print(xArray[1] + ": 10points")
				if(xArray[1]=='Darrell'):
					DarrellScore = DarrellScore + 10
				elif xArray[1]=='Sally':
					SallyScore = SallyScore + 10

	return [DarrellScore, SallyScore, InvalidAno]



Qns = int(input())
inputsStringArray = []

for i in range(0, Qns):
	inputsStringArray.append(input())

Scores = ParserFunction(inputsStringArray)
DarrellScore = Scores[0]
SallyScore = Scores[1]
InvalidAno = Scores[2]
if InvalidAno == 0:
	print('Total Points:')
	if(DarrellScore>=SallyScore):
		print('Sally: ' + str(Scores[1]) + 'points')
		print('Darrell: ' + str(Scores[0]) + 'points')
	elif DarrellScore<SallyScore:
		print('Darrell: ' + str(Scores[0]) + 'points')
		print('Sally: ' + str(Scores[1]) + 'points')


	if DarrellScore == SallyScore:
		print('Game Result: Draw')
	elif SallyScore > DarrellScore:
		print('Game Result: Sally is winner')
	else:
		print('Game Result: Darrell is winner')


