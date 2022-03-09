# dictionary = input()
# string = input()
t = int(input())



for i in range(t):
    ans = ""
    dictionary = input()
    string = input()
    for i in dictionary:
        if i in string:
            ans += i
    print(ans)