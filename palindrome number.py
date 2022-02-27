class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y = str(x)
        if y == y[::-1]:
            return True
        else :
            return False
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
        
#         y = str(x)
#         # lent = len(str(x))
#         for i in range(len(y)):
#             if y[i] == y[len(y)-i-1]:
#                 print(y)
#                 return True
#             else :
#                 return False