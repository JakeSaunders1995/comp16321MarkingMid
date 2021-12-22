import re

hexTextwithPunc = ""
hexText = ""
encryptedFile = "Caesar Cipher(+3):exw fdhvdu lv d olwwoh pruh gliilfxow"
pattern1 = re.compile(r':.+')
matches1 = pattern1.finditer(encryptedFile)

for match in matches1:
    character = match.group()
    hexTextwithPunc = hexTextwithPunc + character

encryptedFile = hexTextwithPunc
pattern0 = re.compile(r'[a-z]+.')
matches0 = pattern0.finditer(encryptedFile)

for match in matches0:
    character1 = match.group()
    hexText = hexText + character1

plaintext = hexText
cipherText = ""
plaintextPosition = 0
while plaintextPosition < len(plaintext):
    plaintextChar = plaintext[plaintextPosition]
    if plaintextChar == " ":
        plaintextPosition += 1
        cipherText = cipherText + " "
        continue

    elif plaintext != " ":
        ASCIIValue = ord(plaintextChar)
        ASCIIValue = ASCIIValue - 3
        cipherText = cipherText + chr(ASCIIValue) 
        plaintextPosition += 1



print (cipherText)