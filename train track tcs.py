


# Incomplete





# from re import A, T


# N = int(input())
# inputdata =[]
# for i in range(N):
#     inputdata.append(input().split(" "))



N = 3
T = [12121,12311,17215]
arrivaltime = [15,5,2]
I = [5,10,3]
F = 12311
starttime = 0
schedule = []
startEnd = []
for i in range(N):
    startEnd.append({arrivaltime[i],arrivaltime[i]+I[i]})
for i in range(N):
    for j in range(i,N):
        if startEnd[i].intersection(startEnd[j]):
            schedule.append( startEnd[i].union(startEnd[j]))
            print(schedule)

# for i in range(N):
#     departuretime.append(arrivaltime[i] + I[i])
#     if min(arrivaltime) > starttime:
#         starttime = arrivaltime

# print(departuretime)
