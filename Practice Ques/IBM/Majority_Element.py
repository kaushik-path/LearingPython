def majority_element(arr): # [2, 2, 1, 1, 1, 2, 2]
    max_count = 0
    max_element = 0
    m = {} 
    for i in arr: # 2, 2, 1, 1, 1, 2, 2
        if i in m: # m[2] = 1, m[2] = 2, m[1] = 1, m[1] = 2, m[1] = 3, m[2] = 3, m[2] = 4
            m[i] += 1
        else:
            m[i] = 1

        if m[i] > max_count: # m[2] = 4 > max_count = 0, m[1] = 3 > max_count = 4
            max_count = m[i]
            max_element = i
    m # Print the frequency map (optional)

    return max_element

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

ans = majority_element(arr)
print(ans)
