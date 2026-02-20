n= int(input("Orginal number: "))
new = int(input("New number: "))
new2 = int(input("New number2: "))
def rev_num(n):
    rev = 0
    l = 0
    while n > 0:
        l = n %10
        rev = rev * 10 + l
        n = n // 10
    return rev

# revNew = new.reverse()
# revNew2 = new2[::-1]

print(f"Reverse of original number is: {rev_num(n)}")
#print("Reverse of new number is: ", revNew)
# print("new REV number2 is: ", revNew2)