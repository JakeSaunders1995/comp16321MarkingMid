#Caesar Cipher

cipherText = input("Enter the word you wish to decrypt: ")
plainText = ""
alphabet = ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
cipherTextPosition = 0

while (cipherTextPosition < len(cipherText)):
	cipherTextChar = cipherText[cipherTextPosition]
	alphabetPosition = 3
	while cipherTextChar != alphabet[alphabetPosition]:
		alphabetPosition += 1

	alphabetPosition = alphabetPosition +3
	plainText = plainText + alphabet[alphabetPosition]
	cipherTextPosition += 1

print("This is your decrypted text: " + (plainText))

#Morse Code

encodedMessage = input("Please enter message to decrypt: ")
morseCode = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f',
             '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
             '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r',
             '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x'}

code = encodedMessage.split()

for i in range(0, len(code)):
    print(morseCode.get(code[i]), end='')


#Hex

def convertHex(hexSubstring):
    return chr(int(hexSubstring, 16))

decodedHex = input("Please enter hex to decrypt: ")
result = ""


for i in range(0, len(decodedHex), 3):
    sub = decodedHex[i] + decodedHex[i+1]
    result += convertHex(sub)

print(result)

