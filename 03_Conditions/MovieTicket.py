age = int(input("enter an age: "))
day = input("Enter a day: ").lower()

price =12 if age >= 18 else 8

if day == "wednesday":
    price-=2

print(f"Ticket Price: ${price}")