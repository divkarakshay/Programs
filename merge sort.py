# code is correct just gives 1 error
l = [90,45,1,7,28,67,2]

def msort(l):
    if len(l) > 1:
        leftarray= l[:len(l)//2]
        rightarray = l[len(l)//2:]
        print(leftarray,rightarray)
        msort(leftarray)
        msort(rightarray)
        i=j=k =0
        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                l[k]=leftarray[i]
                print(l[k],l,"1st while if")
                i=i+1
            else :
                l[k]=rightarray[j]
                print(l[k],l,"1st while else")
                j=j+1
            k=k+1
        while i < len(leftarray):
            l[k]=leftarray[i]
            print(l[k],l,"2nd while")
            i=i+1
        k=k+1
        while j < len(rightarray):
            l[k]=rightarray[j]
            print(l[k],l,"3rd while")
            j=j+1
        k=k+1
    print(l,"final")
    
msort(l)