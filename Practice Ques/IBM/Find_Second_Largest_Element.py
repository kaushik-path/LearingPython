def Find_Second_Largest_Element(arr): # [5, 2, 9, 1, 5, 6]
    largest = float('-inf')
    second_largest = float('-inf')
    if len(arr) <= 2:
        return -1
    for i in range(len(arr)):
        if arr[i] > largest: # 5 > -inf, 2 > 5, 9 > 5, 1 > 9, 5 > 9, 6 > 9
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest: # 2 > -inf, 1 > 2, 6 > 5
            second_largest = arr[i]
    return second_largest

arr = []
n = int(input())
for i in range(n):
    x = int(input())
    arr.append(x)

ans = Find_Second_Largest_Element(arr)
print(ans)