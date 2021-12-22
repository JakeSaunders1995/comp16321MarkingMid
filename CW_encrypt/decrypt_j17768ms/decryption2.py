cipherText = input('CipherText:')
plaintext =""
cipherTextPosition = 0
while (cipherTextPosition <len(cipherText)):
    cipherTextChar = cipherText[cipherTextPosition]
    ASCIIValue = ord(cipherTextChar)
    ASCIIValue = ASCIIValue + 3
    plaintext = plaintext + chr(ASCIIValue)
    cipherTextPosition = cipherTextPosition + 1
print(plaintext)
