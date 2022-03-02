l=[14,46,43,27,57,41,45,21]
def qsort(l):
    length = len(l)
    
    
    if length <= 1:
        return l
    else:
        pivot = l.pop()
    items_grater = []
    items_lower = []

    for item in l:
        if item > pivot:
            items_grater.append(item)
        else:
            items_lower.append(item)
    # print(items_lower,pivot,items_grater)
    return qsort(items_lower) + [pivot] + qsort(items_grater)

print(qsort(l))