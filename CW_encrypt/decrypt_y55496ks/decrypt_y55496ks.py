import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]
file = open(inputFile, "r")

for line in file:
    encryptedLine = line

file.close()

codeType = ""
for i in range(len(encryptedLine)):
    if (encryptedLine[i] != ":"):
        codeType = codeType + encryptedLine[i]
    else:
        break

decryptCode = ""

if codeType == "Hex":
    for i in range(4,len(encryptedLine)):
        if encryptedLine[i] != " ":
            decryptCode = decryptCode + encryptedLine[i]
    decryptCode = bytes.fromhex(decryptCode)
    decryptCode = decryptCode.decode("ascii")
elif codeType == "Caesar Cipher(+3)":
    alphabet = "abcdefghijklmnopqrstuvwxqyz"
    for i in range(17, len(encryptedLine)):
            if encryptedLine[i] == " ":
                decryptCode = decryptCode + " "
            else:   
                for j in range(len(alphabet)):             
                    if encryptedLine[i] == alphabet[j]:
                        decryptCode = decryptCode + alphabet[j-3]  
elif codeType == "Morse Code":
    decryptChar = ""
    morseCodeLine = ""
    charHolder = ""
    morseCode ={'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', 
                '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t',
                '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', '':''}
    for i in range(11, len(encryptedLine)):
        morseCodeLine = morseCodeLine + encryptedLine[i]                  
    for i in morseCodeLine.split("/"):
        decryptChar = i.split(" ")
        for j in range(len(decryptChar)):
            charHolder = decryptChar[j]
            charHolder = morseCode[charHolder]
            decryptCode = decryptCode + charHolder
        decryptCode = decryptCode + " "
    decryptCode = decryptCode.rstrip()

file = open(outputFile, "w")
file.write(str(decryptCode))
file.close()
