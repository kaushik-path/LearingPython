num = int(input())
num1 = num
fac = 1
fac1 = fac

for i in range(1,num):
    fac = fac * num
    num -= 1

while num1 > 0:
    fac1 = fac1 *num1
    num1 -=1

while num1 > 0:
    fac1 *= num1
    num1-=1

print(fac)
print(fac1)