""" half solved """

racedata = {}
racedtemp = []

n = int(input())
t = int(input())
for i in range(1,n+1):
    temp = input().split(" ")
    racedata[i]= [int(i) for i in temp]
# print("racedata",racedata)
for i in range(n):
    var1 = 0
    valu = racedata[i+1]
    print("valu",valu,"valu[n]",valu[n])

    for j in range(0,t+1,2):
        print()
        if j == 0:
            racedtemp.append(0)
        else: 
            print(var1)
            var1 += (valu[n]*valu[j-1]) + (valu[j]*valu[n])
            print(var1)
            racedtemp.append(var1)
            print("i",i,"j",j,"valu[j-1]",valu[j-1],"valu[j]",valu[j],valu[n]*valu[j-1], valu[j]*valu[n],valu[n]*valu[j-1] + valu[j]*valu[n])

# for i in racedata:
#     print(i)       
print(racedtemp)   

# for x,y,z in zip()


"""
3
8
2 2 4 3 5 2 6 2 3
3 5 7 4 3 9 3 2 2
1 2 4 2 7 5 3 2 4

"""