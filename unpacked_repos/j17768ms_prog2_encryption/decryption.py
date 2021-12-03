cipherText = input("CipherText: ")
plaintext = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
cipherTextPosition = 0
while (cipherTextPosition <len(cipherText)):
    cipherTextChar = cipherText[cipherTextPosition]
    alphabetPosition = 3
    while cipherTextChar != alphabet[alphabetPosition]:
        alphabetPosition = alphabetPosition + 1
    alphabetPosition = alphabetPosition + 3
    plaintext = plaintext + alphabet[alphabetPosition]
    cipherTextPosition = cipherTextPosition + 1
print(plaintext)