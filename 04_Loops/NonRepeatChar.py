# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

Name = str(input()).lower()

for char in Name:
    if Name.count(char)== 1:
        print(char)
        break #for only first char we used break
    