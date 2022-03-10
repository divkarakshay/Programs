





otuptu = []
def coins(n):

  if n== 0:
    return 0
  elif 9 <= n :
    otuptu.append(5)
    coins(n-5)
  elif 4<=n :
    otuptu.append(2)
    coins(n-2)
  elif 1 <= n :
    otuptu.append(1)
    coins(n-1)
  return len(otuptu), otuptu.count(5),otuptu.count(2),otuptu.count(1)

print(coins(int(input())))