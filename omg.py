n=list(input("n:"))
vowels="AEIOUaeiou"
i=0
j=len(n)-1
while i<j:
    if n[i] in vowels and n[j] in vowels:
        n[i],n[j]=n[j],n[i]
        result="".join(n)
        print(result)
        break
    elif n[i] not in vowels:
        i+=1
    elif n[j] not in vowels:
        j-=1
    else:
        i+=1
        j-=1
   