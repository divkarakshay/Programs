N = int(input())
amount =(input().split(" "))
print(amount)
P = int(input())
pair = []
for i in range(P):
  pair.append(set(int(x) for x in input().split(" ")))
# print(pair)

# N = 9
# amount = [34,54,65,76,88,23,56,76,43]
# P = 7
# pair = [{1,3},{2,3},{1,2},{6,8},{5,4},{5,7},{8,9}]
toggle = []
ans = []
for i in range(P):
  for j in range(i,P):
    if i != j:
      print(i,j)
      if pair[i].intersection(pair[j]):
        print(pair[i],pair[j])
        if pair[i].union(pair[j]) not in toggle:
          toggle.append(pair[i].union(pair[j]))
print(toggle)
for i in toggle:
  value = 0
  for j in i:
    
    temp = int(j-1)
    print(amount,temp)
    value += int(amount[temp])
  ans.append(value)
print(max(ans))



