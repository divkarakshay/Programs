class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        nege = 1
        if y[0] == "-":
            y = y[:0:-1]
            nege *= -1
            nege = (int(y)*nege)
        else:
            y = y[::-1]
            nege = int(y)
        if nege >= pow(-2, 31) and nege <= (pow(2,31)-1):
            return nege
        else:
            return 0