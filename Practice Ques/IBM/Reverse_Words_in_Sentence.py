def Reverse_Words_in_Sentence(s):
    words = s.split() # ["Hello", "World"]
    reversed_words = words[::-1] # ["World", "Hello"]
    reversed_sentence = ' '.join(reversed_words) # "World Hello"
    return reversed_sentence

s = input()
ans = Reverse_Words_in_Sentence(s)
print(ans)