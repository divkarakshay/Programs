graph = {'A': {'B': 4, 'C': 2},'B': {'D': 10, 'C': 5},'C': {'E': 3},'D': {'F': 4},'E': {'D': 4}}

source, destination = 'A','F'

def shortestPath(source,destination,graph):
  print(source,destination)
  if source in graph.keys() and destination in source :
    print("yes")
  print([(source,Z[destination]) for source, Z in graph.items() if destination in Z])
  # print(True) 
  for source, Z in graph.items():
      print(source,Z)
      if destination in Z:
          print(source,Z[destination],Z)
          
shortestPath(source,destination,graph)
"""*******************************************************"""
d = {'NIFTY': {11382018: 'NIFTY19SEPFUT', 13177346: 'NIFTY19OCTFUT', 12335874: 'NIFTY19NOVFUT'}}

y = 11382018
# print([(k, v[y]) for k, v in d.items() if y in v])+

