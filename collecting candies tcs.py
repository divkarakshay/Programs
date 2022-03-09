







def pickbox(l,sum):
    for i in range(N-1):
        
        first = min(l)
        l.remove(min(l))
        secfirst = min(l)
        l.remove(min(l))
        print(first,secfirst)
        element = first + secfirst
        print(element)
        sum += element
        l.append(element)
        print(l)
    return sum,total
sum = 0
total = []
T = int(input())
for i in range(T):
    N = int(input())
    candies = []
    candies = input().split(" ")
    candies = [int(i) for i in candies]
    print(candies)
    sum,total = pickbox(candies,sum)
    print("answer is", sum)


    


# print(pickbox([1,2,3,4],sum))
