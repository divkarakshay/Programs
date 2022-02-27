class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lent = len(s)
        # lis = [[] for x in numRows]
        resu = ""
        if numRows == 1: return s
        for r in range(numRows):
            inc = 2 * (numRows -1)
            for i in range(r, lent, inc):
                resu += s[i]
                if (r > 0 and r < numRows -1 and i+inc- 2*r < lent):
                    resu += s[i+inc- 2*r]
        return resu