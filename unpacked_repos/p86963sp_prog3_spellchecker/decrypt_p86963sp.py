import sys

def removeAlgorithm(s):
    for i in range(len(s)):
        if (s[i] == ":"):
            return s[i+1 :]

inputFile = sys.argv[1]
outputFile = sys.argv[2]

inputF = open(inputFile, "r")
outputF = open(outputFile, "w")

string = inputF.read()
if (string[0] == "M"):
    encryptedText = removeAlgorithm(string) + " "
    morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e', '..-.':'f','--.':'g','....':'h',
        '..':'i','.---':'j', '-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p',
        '--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z','/':' '
    }

    plainText = ""
    letter = ""
    for character in encryptedText:
        if (character == " "):
            plainText += morse.get(letter)
            letter = ""
            continue
        letter = letter + character
    outputF.write(plainText)

elif (string[0] == "C"):
    encryptedText = removeAlgorithm(string)
    plainText = ""
    cipherTextPos = 0

    while cipherTextPos < len(encryptedText):
        cipherTextChar = encryptedText[cipherTextPos]
        if (cipherTextChar == ' '):
            plainText = plainText + " "
            cipherTextPos += 1
            continue
        ASCIIvalue = ord(cipherTextChar)
        ASCIIvalue = ASCIIvalue - 3
        plainText = plainText + chr(ASCIIvalue)
        cipherTextPos += 1

    outputF.write(plainText)

else:
    encryptedText = removeAlgorithm(string)
    encryptedText = encryptedText.replace(" ", "")
    plainText = bytes.fromhex(encryptedText).decode('utf-8')
    outputF.write(plainText)
