var = 10
num1 = ((var - 1) % 12) + 1
def sum_not_simple(num):
    sum = 0
    for i in range(2, num+1):
        c = True
        for j in range(2, i):
            if i % j == 0:
                c = False
                break
        if not c and num%i==0:
            sum += i
    return sum
print(sum_not_simple(num1))





