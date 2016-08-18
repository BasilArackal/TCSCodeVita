def checkPrime(n):
    flag = 1
    for i in range(2, int(n/2)+1):
        if(n%i==0):
            flag=0
    return flag

val = int(input())
print(checkPrime(2))