plaintext = input('Plaintext:')
cipherText =""
plaintextPosition = 0
while (plaintextPosition <len(plaintext)):
    plaintextChar = plaintext[plaintextPosition]
    ASCIIValue = ord(plaintextChar)
    ASCIIValue = ASCIIValue - 3
    cipherText = cipherText + chr(ASCIIValue)
    plaintextPosition = plaintextPosition + 1
print(cipherText)