





N = int(input())

# def combinations(N):
#     S = [1,2,3]
#     commonsteps = []
# for i in range(N):
#     i
"""**************************************************************************************
"""
def ways(N):
    if N==1 or N==0:
        print("first loop",N)
        return 1
    elif N==2:
        print("second loop",N)
        return 2
    else: 
        return ways(N-3)+ways(N-2)+ways(N-1)
print(ways(N))
"""
*****************************************************************************
"""
# def ways(N):
#     ways = []
#     ways = [0]*(N+1)
#     ways[0] = 1
#     ways[1] = 1
#     ways[2] = 2
#     for i in range(3,N+1):
#         ways[i] = ways[i-3]+ways[i-2]+ways[i-1]
# print(ways(N))