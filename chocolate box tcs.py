l = [1,2,3,4]

def addFtwo(m):
  m.sort()
  if len(m) < 2 :
    return m[0]
  a,b = sum(m[:2]),m[2:]
  b.append(a)
  # print(b)
  return addFtwo(b),a
print(addFtwo(l))

""" 
correct but additional representation required
"""