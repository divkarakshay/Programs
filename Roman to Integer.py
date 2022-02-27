def romanToInt(s):
        a ={'I':1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        c = 0
        for i in range(len(s)-1):
            if a[s[i]]>=a[s[i+1]]:
                c+=a[s[i]]
            else:
                c-=a[s[i]]
        c+=a[s[len(s)-1]]
        return c

romanToInt("MMMDXLI")