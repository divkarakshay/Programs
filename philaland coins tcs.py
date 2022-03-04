
def decimalToBinary(ip_val):
    ste = ""
    if ip_val >= 1:
    # recursive function call
        ste += str(decimalToBinary(ip_val // 2))
        ste += str(ip_val % 2)
    return (ste)
tests = int(input())
for i in range(1,tests+1):
    print(decimalToBinary(int(input())))

    
    
    