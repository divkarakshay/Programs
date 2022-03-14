import numpy as np

def dist_eucl(point1,point2):
  point1 = np.array(point1)
  point2 = np.array(point2)
  return np.linalg.norm(point1-point2)

def collinear(point1,point2,point3):
  count = 0
  if dist_eucl(point1,point2) + dist_eucl(point2,point3) == dist_eucl(point1,point3):
    return count
  else:
    return count+1

def polygon(input_list):
  input_list = input_list + [input_list[0]]
  # print(input_list)
  count = 0
  selected_nodes = {input_list[0]}
  omited_nodes = set()
  for i in range(1,N):
    node1 = input_list[i-1]
    node2 = input_list[i]
    if node2 in omited_nodes:
      continue
    node3 = input_list[i+1]
    # print(node1, node2, node3)
    count = collinear(node1,node2,node3)
    if count :
      selected_nodes.add(node2)
    else :
      omited_nodes.add(node2)
  return len(selected_nodes)

# if __name__ == '__main__':
  # input_1= [(0,0),(0,3),(3,0),(3,1),(3,3)]
N = int(input())
list = []
for i in range(N):
  list1 = input().split()
  print(list1)
  list.append(tuple(int(v) for v in list1))
  # print(list)
print(polygon(list))