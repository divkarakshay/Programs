def SieveOfEratosthenes(n):

  left =[i for i in range(2,n+1)]
  right = []
  # print(left)
  for a in left:
    for i in range(a**2,n+1,a):
      if i not in right:
        right.append(i)
      if i in left:
        # print(i)
        left.remove(i)  
  print(left)
  print(right)

n = 100
SieveOfEratosthenes(n)