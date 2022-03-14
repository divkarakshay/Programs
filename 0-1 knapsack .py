value = [60,100,120]
weight = [10,20,30]
W = 50



def knapsack(val,wt,W,n=len(value)):
    sumv = 0
    sumw = 0
    print(val,wt,W,n)
    
    for i in range(n-1,-1,-1):
        if sumw == W:
            break
        sumw = sumw + wt[i]
        if sumw <= W:
            print(sumw)
    return sumv





knapsack(value,weight,W)
