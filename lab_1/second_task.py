#Variant 6

n="abcdefg"

def prov(n):
    flag = True
    k = ord(n)
    for i in range(1, len(n)):
        if n[i - 1] > n[i]:
            flag = False
    if flag:
        print("Sort")
    else:
        print("Not sort")
