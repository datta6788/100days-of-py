alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# encordec=int(input("what do you wanna do? encrypt/decrypt? to encrypt enter 1 to decrypt enter 0:"))
original=input("enter your message:")
shift=int(input("enter the shift number:"))
# def encrypt(original,shift):
#     enc_text=''
#     extra=int('0')
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

def decrypt(encrypted=original,de_shift=shift):
    dec_text=''
    for letters in encrypted:
        if alphabet.index(letters)>shift:
            if alphabet.index(letters)-shift<=25:
                dec_text+=alphabet[alphabet.index(letters)-shift]
        else:
            dec_loop=shift-alphabet.index(letters)
            while not dec_loop<=25:
                dec_loop=dec_loop-len(alphabet)
            dec_text+=alphabet[dec_loop] 
    print(dec_text)

decrypt(encrypted=original,de_shift=shift)





