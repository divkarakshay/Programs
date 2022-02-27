def divisors(n):
  import math
  
  ans =[]
  sqr = math.ceil(math.sqrt(n))
  for i in range(1,sqr+1):
    if n % i==0:
      if i not in ans:
        ans.append(i)
      if n//i not in ans:
        ans.append(n//i)
  ans.sort()
  return ans