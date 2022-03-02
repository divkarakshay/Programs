l = [85,12,59,45,70,51]
def isort(l):
    for i in range(1,len(l)):
        
        
        # if l[i-1] > l[1]
        currv = l[i]
        curri = i
        while curri > 0 and l[curri-1] > currv:
            print(l[curri-1], ">" ,currv)
            l[curri] = l[curri - 1]
            curri -= 1
        l[curri] = currv
    print(l)
isort(l)


# def insertionSort(nlist):
#    for index in range(1,len(nlist)):

#      currentvalue = nlist[index]
#      position = index

#      while position>0 and nlist[position-1]>currentvalue:
#          nlist[position]=nlist[position-1]
#          position = position-1

#      nlist[position]=currentvalue

# nlist = [14,46,43,27,57,41,45,21,70]
# insertionSort(nlist)
# print(nlist)