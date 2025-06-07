n = int(input())

for i in range(1, 11): 
    if i==4:
        continue
    print(f"{n} X {i} = {n*i}")