alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def encryption(plain_text,shift_key):
    cipherText=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            newPosition=(position+shift_key)%52
            cipherText+=alphabet[newPosition]
        else:
            cipherText+=char
    print(f"Encrypted text:-{cipherText}")

    
def decryption(cipher_text,shift_key):
    plainText=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            newPosition=(position-shift_key)%52
            plainText+=alphabet[newPosition]
        else:
            plainText+=char
    print(f"Decrypted text:-{plainText}")        

 



what_to_do=input("Type 1 for encryption, type 2 for decrryption")
text=input("Type your message:\n")
shift=int(input("Enter shift key:\n"))
if what_to_do=='1':
    encryption(text,shift)
elif what_to_do=='2':
    decryption(text,shift)
