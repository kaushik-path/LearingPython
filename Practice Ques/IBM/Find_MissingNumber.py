def Find_Missing_Number(arr):
    n = len(arr) + 1 # If the array has n-1 elements, then the total number of elements should be n (including the missing number)
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum
        
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

ans1 = Find_Missing_Number(arr)
print(ans1)