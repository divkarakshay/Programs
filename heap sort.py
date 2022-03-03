from turtle import right


l = [14,46,43,27,57,41,45,21,70]
def maxheap(l,length,parentidx):
    largest = parentidx


    left = 2*parentidx +1
    right = 2*parentidx +2
    if left < length and l[left] > l[largest]:
        largest = left
    if right < length and l[right] > l[largest]:
        largest = right
    if largest != parentidx:
        l[largest], l[parentidx] = l[parentidx],l[largest]
        maxheap(l,length,parentidx)
def hsort(l):
    length = len(l)


    for i in range(length//2 - 1,-1,-1):
        print(i,l[i])
        maxheap(l,length,i)
    for i in range(length-1,0,-1):
        l[length],l[0] = l[0],l[length]
        maxheap(l,i,0)
    return l
print(hsort(l))