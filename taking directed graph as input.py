graph = {}
def addEdges(k,v):
  if k not in graph:
    graph[k] = (v)
  elif type(graph[k]) == list :
    print(f"{k} already exist")
    graph[k].append(v)
  else :
    graph[k] = [graph[k],v]

N = int(input("enter integer of total no. of edges"))
for i in range(N):
  k,v = input(" enter pair of  & node points (eg. 3 8)").split()
  addEdges(k,v)
print(graph)