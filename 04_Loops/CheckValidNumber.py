# Enter a num b/w 1 to 10: 89
# Try again
# Enter a num b/w 1 to 10: 76
# Try again
# Enter a num b/w 1 to 10: 54
# Try again
# Enter a num b/w 1 to 10: 2
# Ok ha ji

while True:
    num = int(input("Enter a num b/w 1 to 10: "))
    if 1 <= num <= 10:
        print("Ok ha ji")
        break
    else:
        print("Try again")