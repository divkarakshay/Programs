class Solution(object):
    def myAtoi(self, s):
        r = ""
        sign = ""
        Number_Start = False
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        for i in s:
            if i in numbers:
                Number_Start = True
                r+= i
            elif i == "-":
                if Number_Start:
                    break
                else:
                    Number_Start = True
                if sign == "":
                    sign = "-"
                else:
                    return 0
            elif i == "+":
                if Number_Start:
                    break
                else:
                    Number_Start = True
                if sign == "":
                    sign = "+"
                else:
                    return 0
            elif i == " ":
                if Number_Start:
                    break
                pass
            else:
                break
        if r == "":
            return 0
        if sign == "-":
            sign += r
            if int(sign) <= -2147483648:
                return -2147483648
            return int(sign)
        if int(r) >= 2147483648:
            return 2147483647
        return int(r)

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s=s.strip()
#         if not s:
#             return 0
#         nagetive = False
#         out = 0
#         if s[0] == "-":
#             nagetive = True
#         elif s[0] == "+":
#             nagetive = False
#         elif not s[0].isnumeric :
#             return 0
#         else:
#             out = ord(s[0]) - ord("0")
#         for i in range(1,len(s)+1):
#             if s[i].isnumeric():
#                 out = out*10 + (ord(s[i]) - ord("0"))
#                 if not nagetive and out >= 2147483647 :
#                     return 2147483647
#                 if nagetive and out>= 2147483647:
#                     return -2147483647
#             else :
#                 break
#             if not nagetive :
#                 return out
#             else :
#                 return -out
#             