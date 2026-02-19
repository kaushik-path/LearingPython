n = int(input())
arr= []
for i in range(n):
    arr.append(int(input()))

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

storeArr = sort_array(arr)
print(arr)
print(storeArr)
print(arr[-1])
print(storeArr[-1])