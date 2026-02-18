# words=['hello','world','green']
# dash=""
# print(words[2])
# for d in words[2]:
#     dash+="_"
# print(dash)
# show=""
# display=''
# for word in words[2]:
#     display+=word
# while display!=show:
#     user=input("guess a letter:")
#     if user in display:
#         show+=user
#     print(show)
# print("you won!")


# D="asshole"
# print(D[0])

# words=['hello','world','green']
# dash=""
# print(words[2])
# for d in words[2]:s
#     dash+="_"
# print(dash)
# i=len(words[2])
# show=""
# display=''
# for word in words[2]:
#     display+=word
# while display!=show:
#     user=input("guess a letter:")
#     for letter in range(i):
#         if display[letter]==user:
#             show+=user
#             i-=1
#     print(show+dash[0:i])
    
# print(show)
# print("you won!")

# user=input("guess a letter:")
# for letter in animals:
#     if letter==user:
#         output+=user
#     else:
#         output+="_"
# print(output)

# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letter: ").lower()

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         game_over = True
        # print("You win.")

# so this is not the full code for the hangman game, why the elif statement is used?

# D=input("enter")
# if "_" in D:
#     print("you entered a blank")
# else:print("goodboyy")


##############################################################
##############################################################
##############################################################
# words=['hello','world','elephant']
# dash=""
# print(words[2])
# for d in words[2]:
#     dash+="_"
# print(dash)
# length=len(words[2])
# i=len(words[2])
# show=""
# display=''
# correct=[]
# for word in words[2]:
#     display+=word
# while display!=show:
#     showing=""
#     user=input("guess a letter:")
#     for letter in range(length):
#         if display[letter]==user:
#             showing+=user
#             correct.append(user)
#         elif display[letter] in correct:
#             showing+=display[letter]
#         else:
#             showing+="_"
#     print(showing)
#     if showing==display:
#         display=show
# print("you won")
###########################################################
###########################################################
###########################################################


# import random

# words=['KITAGAWA','GOKU','RENGOKU','GOJO','TANJIRO','ZORO','LUFFY']
# dash=""
# comp_choice=random.choice(words).lower()
# print(comp_choice)
# import omg
# print(omg.words)

# import omg
# print(omg.words)

# import random
# D=["kuber","datta","vardhan"]
# guess=""
# ran=random.choice(D)
# for name in range(len(ran)):
#     guess+=
# print(guess)
# print(D[random.randint(0,2)])
# d=["datta","sabrina","meganfox","kuber","keerthi","vardhan","krish","meganfox"]
# e=random.choice(d)
# guess=[]
# final=""
# for name in e:
#     guess.append(name)
# f=random.shuffle(guess)
# for letters in guess:
#     final+=letters
# print(e)    
# print(final)    
# print(guess)

# print(d.index("meganfox"))

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    
# # print(alphabet.index('cd'))
# # d=input(int("give ra give:"))
# number=int('0')
# d=int(input('give:'))
# number+=d
# e=int(input('give:'))
# number+=e
# print(number)


# print(len(alphabet))
#######################################################
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # encordec=int(input("what do you wanna do? encrypt/decrypt? to encrypt enter 1 to decrypt enter 0:"))
# original=input("enter your message:")
# shift=int(input("enter the shift number:"))
# def encrypt(original,shift):
#     enc_text=''
#     for letter in original:
#         shift_pos=alphabet.index(letter)+shift
#         if shift_pos<=25:
#             enc_text+=alphabet[shift_pos]
#         else:
#             shift_pos%=len(alphabet)
#             enc_text+=alphabet[shift_pos]
            
#     print(enc_text)
# encrypt(original,shift)


# def encrypt(original,shift):
#     enc_text=''
#     for letter in original:
#         if alphabet.index(letter)+shift<=25:
#             enc_text+=alphabet[alphabet.index(letter)+shift]
#         else:
#             loop=alphabet.index(letter)+shift
#             while not loop<=25:
#                 loop=loop-len(alphabet)
#             enc_text+=alphabet[loop]
#     print(enc_text)
# encrypt(original,shift)

# def decrypt(encrypted=original,de_shift=shift):
#     dec_text=''
#     for letters in encrypted:
#         dec_shift=alphabet.index(letters)-shift
#         dec_shift%=len(alphabet)
#         dec_text+=alphabet[dec_shift]
#     print(dec_text)

# decrypt(encrypted=original,de_shift=shift)


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# d=input("enter ra enter:")
# text=''
# for letter in d:
#     if letter in alphabet:
#         text+=letter
#     else:
#         text+="&"
# print(text)


