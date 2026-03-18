def Check_Valid_Anagram(s1, s2):
    if len(s1) != len(s2): 
        return False
    return sorted(s1) == sorted(s2) # sorted("listen") == sorted("silent")

s1 = input()
s2 = input()
ans= Check_Valid_Anagram(s1, s2)
print(ans)