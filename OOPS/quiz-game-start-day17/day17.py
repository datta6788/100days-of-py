n=80085
num_str=str(n)
count=0
for i in range(len(num_str)-1):
    d=int(num_str[i])
    if d!=0 & n%d==0:
        count+=1
count