alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
d=input("enter ra enter:")
for letter in d:
    text=""
    if letter in alphabet:
        text+=letter
    else:
        text+="&"
print(text)