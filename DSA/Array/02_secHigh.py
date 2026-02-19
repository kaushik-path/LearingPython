n = int(input())
arr = []
for i in range(n):
    arr.append(int(input())) # 4 0 5 1 

def second_highest(arr):
    first = second = float('-inf')
    for i in arr:
        if i > first:  # 1: num = 4 > first = -inf
            second = first # 2: second = -inf
            first = i # 3: first = 4
        elif first > i > second:
            second = i
    return second

print(second_highest(arr))