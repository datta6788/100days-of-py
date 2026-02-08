# cars=["TATA","BMW","Toyota","Audi"]
# for car in cars:
#     print(car)

# marks=[35,5]
# total=(marks)
# print(total)


# marks=[12,12]
# product=1
# for numbers in marks:
#     product*=numbers
# print(product)

# num=[2,4,1,5,6,9,69,0,22,34,55,11,22,44,]
# max=0
# for numbers in num:
#     if numbers>=max:
#         max=numbers
# print(max)

# add=0
# for num in range(0,101):
#     add+=num
# print(add)

# for num in  range(1,10):
#     if num==2:
#         print("datta")
#     else: print(num)

################FizzBuzz############
# for num in  range(1,101):
#     if num%3==0 or num%5==0:
#         if num%3==0 and num%5==0:
#             print("FizzBuzz")
#         elif num%3==0:
#             print("Frizz")
#         elif num%5==0:
#             print("Buzz")
#     else:
#         print(num)


# import random
# letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# num=['0','1','2','3','4','5','6','7','8','9']
# symb=['!','@','#','$','%','^','&','*','(',')','_','+']
# print("pASSword ZENrator")
# password=[]
# no_letters=int(input("enter no of letters:"))
# no_num=int(input("enter no of numbers:"))
# no_symb=int(input("enter no of symbols:"))
# for letter in range(1, no_letters + 1):
#     D=random.choice(letters)
#     password+=D
# for number in range(1, no_num+1):
#     E=random.choice(num)
#     password+=E
# for symbol in range(1,no_symb+1):
#     F=random.choice(symb)
#     password+=F
# print(password)
# random.shuffle(password)
# print(password)
# finalPass=""
# for pASS in password:
#     finalPass+=pASS
# print(finalPass)

# import random
# DD=""
# D=int(input("no:"))
# dd=['0','1','2','3','4','5','6','7','8','9']
# for no in range(1,D+1):
#     DD+=dd[no]
# print(DD)