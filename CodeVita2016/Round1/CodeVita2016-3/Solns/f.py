# 0< T<=10
# 0< N <=200
# 0<= E <=N*N 

def magic(N, E):
	#print(T)
	

def check4Constraints(N, E):
	if(0>=N or N>200 or 0>E or E>N*N):
		print("Invalid Input")
		return 0
	else:
		return 1


#Read T inputs to Array of N & E
T = int(input())
N=[]
E=[]
for i in range(0, T):
	NT, ET=input().split()
	NT = int(NT)
	ET = int(ET)
	N.append(NT)
	E.append(ET)

#Main loop to iterate through all the Values of N & E
for i in range(0, T):
	if(check4Constraints(N[i], E[i])==1):
		magic(N[i], E[i])

