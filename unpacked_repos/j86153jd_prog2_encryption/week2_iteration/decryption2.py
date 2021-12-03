ciphertext=input("Please enter some ciphertext: ")
plaintext=""
ciphertextPosition=0
while ciphertextPosition<len(ciphertext):
    ciphertextChar=ciphertext[ciphertextPosition]
    ASCIIValue=ord(ciphertextChar)
    ASCIIValue+=3
    plaintext=plaintext + str(chr(ASCIIValue))
    ciphertextPosition+=1
print(plaintext)
