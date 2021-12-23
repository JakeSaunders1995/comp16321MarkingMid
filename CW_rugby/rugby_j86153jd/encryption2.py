plaintext=input("Please enter some plaintext: ")
cipherText=""
plaintextPosition=0
while plaintextPosition<len(plaintext):
    plaintextChar=plaintext[plaintextPosition]
    ASCIIValue=ord(plaintextChar)
    ASCIIValue-=3
    cipherText=cipherText + chr(ASCIIValue)
    plaintextPosition+=1
print(cipherText)
