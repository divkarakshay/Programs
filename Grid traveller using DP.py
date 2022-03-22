def gridTraveller(m, n):
    if n==0 or m==0 : return 0
    if n==1 and m==1 : return 1
    return gridTraveller(m-1,n) + gridTraveller(m,n-1)



def gridTraveller1(m, n, memo={}):
    key = str(m) + "," + str(n)
    if key in memo: return memo[key]
    if n==0 or m==0 : return 0
    if n==1 and m==1 : return 1
    memo[key] = gridTraveller1(m-1,n,memo) + gridTraveller1(m,n-1,memo)
    print(memo)
    return memo[key]


print(gridTraveller(4,6))


print(gridTraveller1(18,18))