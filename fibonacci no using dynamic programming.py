






def fib(n,memoization ={}):
  
  if n in memoization:
    return memoization[n]
  print("memo of n ",memoization[n])
  if n <= 2:
    return 1
  print("memo all",memoization)
  memoization[n] = fib(n-1,memoization)+fib(n-2,memoization)
  print(" all memo",memoization)
  return memoization[n]

# print(fib(8))
print(fib(50))
