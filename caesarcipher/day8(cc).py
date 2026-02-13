alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
enc_or_dec=int(input("what do you wanna do? encrypt/decrypt? to encrypt enter 1 to decrypt enter 0:"))
org_text=input("enter your message:")
shift=int(input("enter the shift number:"))
def ceasercpher(org_text,shift,enc_or_dec):
    text=""
    for letter in org_text:
        if enc_or_dec==1:
            shift_pos=alphabet.index(letter)+shift
            shift_pos%=len(alphabet)
            text+=alphabet[shift_pos]
        else:
            shift_pos=alphabet.index(letter)-shift
            shift_pos%=len(alphabet)
            text+=alphabet[shift_pos]
    print(text)
ceasercpher(org_text,shift,enc_or_dec)








