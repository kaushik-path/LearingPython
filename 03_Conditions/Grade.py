score = int(input("Enter marks: "))

if score >= 101:
    print("NAN")
    exit()

if score > 90:
    grade = "O"
elif score >= 81:
    grade = "A+" 
elif score >= 71:
    grade = "A"
elif score >= 61:
    grade = "B+"
elif score >= 51:
    grade = "B"
elif score >= 41:
    grade = "C"
elif score >= 34:
    grade = "D"
else:
    grade= "F"

print(grade)