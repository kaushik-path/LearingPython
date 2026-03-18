def Character_Frequency_in_String(s):
    s = s.lower()
    s = s.replace(" ", "")
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

s= input()
ans = Character_Frequency_in_String(s)
print(ans)