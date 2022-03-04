# answer is not correct






from math import sqrt
lost=[]
def prime(n,m=2):
    

    for i in range(m,n+1):
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break
            else:
                # print(i)
                lost.append(i)
    print(lost)
    return lost

def primeFibonacci(a,b):
    primelist = prime(b,a)
    multiplicationlist = []
    newlist = []
    for i in primelist:
        for j in primelist:
            if i != j:
                multiplicationlist.append(i*j)
    print(multiplicationlist)
    for i in multiplicationlist:
        for j in range(2,int(i**1/2)+1):
            if i % j==0:
                break
            else:
                if i not in newlist:
                    newlist.append(i)
    print(newlist)

primeFibonacci(int(input("First NO:")),int(input("Second NO:")))