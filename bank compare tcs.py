





amount = int(input())
tenture = int(input())
print(amount,tenture)
bank = []
for i in range(2):
    sum1 = 0
    for j in range(int(input())):
        yrs,slab = [float(v) for v in input().split()]
        yrs = int(yrs)
        sq = (1-slab)**(yrs * 12)
        emi = (amount * slab)/(1-1/sq)
        sum1 = sum1 + emi
    bank.append(sum1)
if bank[0] < bank[1]:
    print("Bank A")
else:
    print("Bank B")
