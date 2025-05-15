nums = [] #empty array
n = int(input("Enter how many numbers: ")) #take input how many number need
positive_count = 0
positive_Int = []

for i in range(n):
    #num = int(input(f"Enter number {i + 1}: "))
    num = int(input())
    nums.append(num)

for num in nums:
    if num > 0:
        #print(num)
        positive_Int.append(num)
        positive_count += 1

print("Count of positive numbers:", positive_count)
print("All Positive numbers entered:", positive_Int)
print("All numbers entered:", nums)