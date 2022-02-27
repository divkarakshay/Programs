class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0 :
            print("divisible")
            hal=(len(nums1))//2
            print(nums1[hal])
            return (nums1[hal] + nums1[hal - 1])/2
        else:
            hal=(len(nums1)-1)//2
            return nums1[hal]
#         nums1.extend(nums2)
#         nums1.sort()
        
#         print(nums1)
#         ans = sum(nums1)/len(nums1)
        # return ans