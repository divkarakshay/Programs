class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointers 
        first, last = 0 , len(height)-1
        _ = 0
        # While they do not cross keep moving 
        while first < last:
            new_height = 0
            # If one side is smaller move that side 
            if height[first] < height[last]:
                new_height = height[first] 
                first+=1
            else:
                new_height = height[last]
                last-=1
            # Calculate the area and store only the max 
            area = new_height * (last-first + 1)
            _ = max(area,_)
        return _
# def maxArea(height):
#   print("list",height)
#   result = []
#   for i,k in enumerate(height):
#     for j in range(len(height)):
#       if j<i:
#         print(k,i,j,((k) * (i-j)))
#         result.append(min(k,height[j]) * (i-j))
#   print(result)
#   print(max(result))

maxArea([1,2,1])
maxArea([1,8,6,2,5,4,8,3,7])