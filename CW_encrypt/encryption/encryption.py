plaintext=input("Please enter some plaintext: ")
cipherText=""
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintextPosition=0
while plaintextPosition<len(plaintext):
    plaintextChar=plaintext[plaintextPosition]
    alphabetPosition=0
    while plaintextChar!=alphabet[alphabetPosition]:
        alphabetPosition+=1
    alphabetPosition-=3
    cipherText=cipherText + alphabet[alphabetPosition]
    plaintextPosition+=1
print(cipherText)
