plaintext = ""
cipherText = input("CipherText:")
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
ciphertextPosition = 0
while ciphertextPosition < len(cipherText):
	ciphertextChar = cipherText[ciphertextPosition]
	alphabetPosition = 3
	while ciphertextChar.upper() != alphabet[alphabetPosition]:
		alphabetPosition += 1
	alphabetPosition += 3
	plaintext = plaintext + alphabet[alphabetPosition]
	ciphertextPosition += 1
print(plaintext)