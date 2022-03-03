# there is one silly mistake in code need to be addressed 
l= [4,5,1,2,3]
def ssort(l):
  n = len(l)
  small = n-1
  for i in range(n):
    for j in range(i,n):
      print(l[j])
      if l[j] <l[small]:
        small = j
        print("small", small,l[small])
        l[small],l[i] = l[small],l[i]
        small = n-1
        print(l)
  print("final",l)


print(ssort(l))

# def selectionSort(nlist):
#    for fillslot in range(len(nlist)-1,0,-1):
#        maxpos=0
#        for location in range(1,fillslot+1):
#            if nlist[location]>nlist[maxpos]:
#                maxpos = location

#        temp = nlist[fillslot]
#        nlist[fillslot] = nlist[maxpos]
#        nlist[maxpos] = temp

# nlist = [14,46,43,27,57,41,45,21,70]
# selectionSort(nlist)
# print(nlist)