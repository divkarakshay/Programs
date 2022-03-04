def decimalToBinary(ip_val):
    ste = ""
    if ip_val >= 1:
    # recursive function call
        ste += str(decimalToBinary(ip_val // 2))
    
    # printing remainder from each function call
    # print(ip_val % 2, end = '')
        ste += str(ip_val % 2)
    return (ste)

print(decimalToBinary(int(input("Enter Decimal no. to convert to Binary"))))