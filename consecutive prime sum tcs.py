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
    return lost


def consicutiveprime(n):
    m=0
    loist = prime(n,m)
    print(loist)
    m=0
    for i in range(2,len(loist)):
        sume = 0
        for j in loist:
            sume += j
            if sume == loist[i]:
                m +=1
                break
            if sume > loist[i]:
                break
    print(m)
    return m

n=int(input())
consicutiveprime(n)