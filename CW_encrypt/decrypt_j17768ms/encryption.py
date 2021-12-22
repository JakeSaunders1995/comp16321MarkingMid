plaintext = input("PlainText: ")
cipherText = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
plaintextPosition = 0
while (plaintextPosition <len(plaintext)):
    plaintextChar = plaintext[plaintextPosition]
    alphabetPosition = 3
    while plaintextChar != alphabet[alphabetPosition]:
        alphabetPosition = alphabetPosition + 1
    alphabetPosition = alphabetPosition - 3
    cipherText = cipherText + alphabet[alphabetPosition]
    plaintextPosition = plaintextPosition + 1
print(cipherText)