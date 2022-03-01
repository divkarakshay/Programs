ip = "345564"

def opt(ip):
    preotp = ""
    for i in range(1,len(ip),2):
        if not i:
            print('empty')
            break

        else:
            preotp += str(int(ip[i]) ** 2)
    # print(preotp)
    if len(preotp) >= 4:
        return preotp[:4]
    else :
        return -1


print(opt(ip))