def encrypter(msg, uid, uidLen):
	listofmsg = list(msg)
	pt1 = str(uidLen) + '-' + str(uid) 
	for i in range(0, len(listofmsg)):
		listofmsg[i] = format(ord(listofmsg[i]), "x").upper()[::-1]
	pt2 = '-'.join(listofmsg)
	finalpart = pt1 + '-' + pt2
	print(finalpart)

def decrypter(msg):
	splitMsg = msg.split('-')
	print(splitMsg[1])
	splitMsg =splitMsg[2:]
	for i in range(0, len(splitMsg)):
		splitMsg[i] = splitMsg[i][::-1]
		splitMsg[i] = chr(int(splitMsg[i], 16)) 
	print(''.join(splitMsg))

initalInput = input()
if(initalInput == 'E'):
	inString = input()
	uniqueID = input()
	uniqueIDLength = len( str(uniqueID) )
	encrypter(inString, uniqueID, uniqueIDLength)
else:
	dString = input()
	decrypter(dString)
