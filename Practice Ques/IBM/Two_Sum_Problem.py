def Two_Sum_Problem(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return -1

n= int(input())
arr=[]
for i in range(n):
    x= int(input())
    arr.append(x)

target = int(input())
ans = Two_Sum_Problem(arr, target)
print(ans)