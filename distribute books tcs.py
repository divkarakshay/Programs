


"""
*********************** Recursion *******************************
"""
N = int(input())
def destri(N):
    if N==0:
        return 1
    if N==1:
        return 0
    if N==2:
        return 1
    return (N-1)*(destri(N-1) + destri(N-2))
print(destri(N)%1000000007)
"""
***************** Dynamic Programing *****************************
"""
def destribution(n):
    d=[0 for i in range(n+1)]
    d[0]=1
    d[1]=0
    d[1]=1

    for i in range(3,(n+1)):
        d[i]=(i-1)*(d[i-1]+d[i-2])
    return d[n]
# n = int(input())
print(destribution(N)%1000000007)