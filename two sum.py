class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print (List)
        premap = {} #val : index
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in premap:
                return [premap[diff],i]
            premap[n] = i
            # print(premap)
        return
            # print(i,n)
            