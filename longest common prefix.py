class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        prefix = strs[0]
        for i in range(1, len(strs)):
            while(strs[i][:len(prefix)]!=prefix):
                prefix = prefix[:-1]
                strs[i] = strs[i][:-1]
        return prefix

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         print(strs)
#         s = []
#         sl=""
#         print(range(len(min(strs, key=len))))
#         for a in range(1,len(strs)):
#             for i in range(len(min(strs, key=len))):
#                 print(a,i)
#                 if strs[0][i]==strs[a][i]:
#                     type(sl)
#                     type(strs[0][i])
#                     sl += strs[0][i]
#                 s.append(sl)
#                 sl = 0

#                 print(s)
                    
                
                