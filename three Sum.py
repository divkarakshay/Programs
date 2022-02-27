# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         op = []
#         nums.sort()
#         print(nums)
#         for i in range(len(nums)):
#         # print(i)
#             for j in range(len(nums)) :
#                 for k in range(len(nums)):
#                     if nums[i]+nums[j]+nums[k]==0 and nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k] :
#                         if sorted([nums[i],nums[j],nums[k]]) not in op :
#                             op.append(sorted([nums[i],nums[j],nums[k]]))
#         return(op)
def threeSum(nums):
  op = []
  # nums = list(set(nums))
  nums.sort()
  print(nums)
  for i in range(len(nums)):
    if i>0 and nums[i] == nums[i-1]: continue
    l= i+1
    r= len(nums)-1
    print(i,l,r)
    while l<r:
      if nums[i]+nums[l]+nums[r]==0:
        op.append([nums[i],nums[l],nums[r]])
        while (l<r and nums[l] == nums[l+1]):
          l+=1
        while (l<r and nums[r] == nums[r-1]):
          r-=1
        l+=1
        r-=1
      elif nums[i]+nums[l]+nums[r]>0:
        r-=1
      else :
        l+=1
  return op

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-2,0,0,2,2]))