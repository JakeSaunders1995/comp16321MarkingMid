import sys
import os

def getArguments():
    arguments = sys.argv
    source = arguments[1]
    destination = arguments[2]
    return source, destination

def readCipherText(fileName):
    file = open(fileName)
    cipherText = file.read()
    file.close()
    return cipherText

def readFormat(text):
    divisionLocation = text.index(':')
    algorithm = text[0:divisionLocation]
    cipherText = text[divisionLocation+1:]
    return algorithm, cipherText

def decryption(method, cipherText):
    plainText = ""
    characterList = []
    if (method == "Morse Code"):
        # morse code
        morseCodeDict = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0"}
        count = 0
        string = ""
        # seperate each character and appends to list
        for i in range(len(cipherText)):
            if cipherText[i] != ' ':
                string += cipherText[i]
            else:
                characterList.append(string)
                string = ""
        characterList.append(string)

        # convert each character from morse code into english
        for character in characterList:
            if character == "/":
                plainText += " "
            else:
                plainText += morseCodeDict[character]

    elif (method == "Caesar Cipher(+3)"):
        # caesar +3
        for i in range(len(cipherText)):
            ASCIIValue = ord(cipherText[i])
            if (ASCIIValue == 32 or cipherText[i] == "\n"):
                # if [SPACE] or [NEW LINE} keep the same
                plainText += chr(ASCIIValue)
            else:
                ASCIIValue -= 3
                # accounts for first letters moving to end of alphabet
                if (ASCIIValue == 96):
                    ASCIIValue = 122
                elif (ASCIIValue == 95):
                    ASCIIValue = 121
                elif (ASCIIValue == 94):
                    ASCIIValue = 120
                plainText += chr(ASCIIValue)
    elif (method == "Hex"):
        # hex
        cipherText = cipherText.replace(" ","")
        # splits cipher text into list of 2-digit hex numbers
        for i in range(int(len(cipherText)/2)):
            characterList.append(cipherText[i*2: i*2+2])
        # converts each hex number into characters and adds to plaintext
        for character in characterList:
            plainText += chr(int(character, 16))
    return plainText

def writeResult(fileName, iPath, oPath, result):
    fName = fileName.replace(".txt", "_f18903ls.txt")
    os.chdir(oPath)
    file = open(fName, "w")
    file.write(result.lower())
    file.close()
    os.chdir(iPath)

#main
source, destination = getArguments()

#calculate number of files in dir and adds to fileList and creates relative paths
fileList = []
pathOfCurrentFile = os.path.dirname(os.path.abspath("decrypt_f18903ls.py"))
sourcePath = os.path.join(pathOfCurrentFile, source)
destinationPath = os.path.join(pathOfCurrentFile, destination)
for file in os.listdir(os.path.join(sourcePath)):
    fileList.append(file)

os.chdir(sourcePath)
for file in fileList:
    ct = readCipherText(file)
    algo, ct = readFormat(ct)
    pt = decryption(algo, ct)
    writeResult(file, sourcePath, destinationPath, pt)
