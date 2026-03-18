n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
print(arr)
print(arr[-1]) # Print the largest element
print(arr[-2]) # Print the second largest element