# bubble sort using recurance
l = [50,3,9,34,1]

def bsort(l):
    b = 0
    size = len(l)
    for i in range(size-1):
        b = b + 1
        if l[i] > l[i+1]:
            temp = l.pop(i+1)
            l.insert(i,temp)
            bsort(l)
            # print(l)
    return(l)
    
print(bsort(l))

"""[50,3,9,34,1]"""