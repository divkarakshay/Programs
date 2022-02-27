# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         length = len(s)
#         lis=[]
#         for i,c in enumerate(s):
#             print("i",i)
#             for j in range(0,length):
#                 print("j",j)
#                 if i-j >= 0 and i+j <= length and s[i-j] == s[i+j]:
#                     if s[i-j:i+j+1] not in lis:
#                         lis.append(s[i-j:i+j+1])
#                     print(lis)
#         lis.sort(reverse=True)
#         print(lis)
#         return lis[0]

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resl = 0
        leng = len(s)
        for i in range(leng):
            # for odd length
            l, r = i, i
            while l >= 0 and r < leng and s[l] == s[r]:
                if (r - l + 1) > resl:
                    res = s[l:r+1]
                    resl = r - l + 1
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < leng and s[l] == s[r]:
                if (r - l + 1) > resl:
                    res = s[l:r+1]
                    resl = r - l + 1
                l -= 1
                r += 1
        return res
            #for even length
            
                
            # print(res)
        # return find(s)
        