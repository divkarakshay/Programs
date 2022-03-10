





S, R= input().split()
S, R = int(S), int(R)
# samples = input().split()
samples =[ int(i) for i in input().split()]
print(samples)
for i in range(R):
    c1 = 0
    b1, b2= input().split()
    b1, b2= int(b1), int(b2)
    for i in samples:
        if i > b1 and i < b2:
            c1 += 1
    print(c1)
