from operator import index


N = 4
opponents = [7,8,9]
sums =0
temp = 0

def iter(l,sums):
  max = l[0]
  altMax = l[0]
  ialtmax = 0
  if len(l) > 2:
    for i in range(len(l)):
      if l[i] > max:
        max = l[i]
    for i in range(len(l)):
      if l[i] > altMax and l[i] != max:
        altMax = l[i]
        ialtmax = i
    if l[ialtmax - 1] < l[ialtmax + 1]:
      sums += (altMax * l[ialtmax + 1]) - l[ialtmax - 1]
      print("removed",altMax)
      print(sums)
      l.remove(altMax)
      iter(l,sums)
    else:
      sums += (altMax * l[ialtmax + 1]) - l[ialtmax - 1]
      print("removed",altMax)
      print(sums)
      l.remove(altMax)
      iter(l,sums)

    # iter(l)
  
  if len(l) == 2:
    if l[0] < l[1]:
      sums += l[0] * l[1]
      print("removed",l[0])
      print(sums)
      l.pop(0)
    else:
      sums += l[0] * l[1]
      print("removed",l[1])
      print(sums)
      l.pop(1)
    iter(l,sums)
  
  if len(l) == 1:
    sums += l[0]
    print("removed",l[0])
    print(sums)
    l.pop(0)
    print("returning")
  return sums

  
print(iter(opponents,sums))
