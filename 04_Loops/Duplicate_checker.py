items= input().split()

unique = set()

for item in items:
    if item in unique:
        print("Duplicate: ", item)
        break
    unique.add(item)
else:
    print("no Duplicate")