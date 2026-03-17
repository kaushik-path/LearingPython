def First_NonRepeating_Character(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return -1

s= input()
result = First_NonRepeating_Character(s)
print(result)
