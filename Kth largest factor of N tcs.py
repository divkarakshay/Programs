N,K = input().split(" ")
N,K = int(N),int(K)
list = []




for i in range(1,int(N/2) + 1):
    # print("loop")
    if N % i == 0:
        list.append(i)
        # print(i)
list.append(N)
if len(list) > K :
    print(list[K])
else :
    print(1)