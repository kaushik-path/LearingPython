def Move_All_Zeros_to_End(arr): # [0, 1, 0, 3, 12]
    count = 0
    for i in range(len(arr)): # 0 != 0, 1 != 0, 0 != 0, 3 != 0, 12 != 0
        if arr[i] != 0:
            arr[count] = arr[i] # arr[0] = 1, arr[1] = 3, arr[2] = 12
            count += 1

    while count < len(arr): # arr[3] = 0, arr[4] = 0
        arr[count] = 0
        count += 1
    return arr

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

ans = Move_All_Zeros_to_End(arr)
print(ans)