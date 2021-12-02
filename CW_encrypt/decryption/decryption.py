ciphertext=input("Please enter some ciphertext: ")
plainText=""
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertextPosition=0
while ciphertextPosition<len(ciphertext):
    ciphertextChar=ciphertext[ciphertextPosition]
    alphabetPosition=0
    while ciphertextChar!=alphabet[alphabetPosition]:
        alphabetPosition+=1
    alphabetPosition+=3
    plainText=plainText + alphabet[alphabetPosition]
    ciphertextPosition+=1
print(plainText)
