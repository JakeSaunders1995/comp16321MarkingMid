import os, sys

for file in (os.listdir(sys.argv[1])):
    f = open(os.path.join(sys.argv[1],file),"r")
    textFile = f.read()
    f.close()

    def seperateWords(text):
        return(text.split())

    def getFirstWord(character, finish):
        if finish == False:
            return(character)
        else:
            return("skip")
        
    firstWord = ""

    colonFound = False
    counter = 0
    for i in textFile:
        counter += 1
        if i == ":":
            colonFound = True
            colonCounter = counter
        character = getFirstWord(i, colonFound)
        if character != "skip":
            firstWord = firstWord + character


    textFileList = seperateWords(textFile[colonCounter:])

    decyptedText = ""
    if firstWord == "Hex":
        for i in textFileList:
            decyptedText = decyptedText + bytearray.fromhex(i).decode()

    elif firstWord == "Caesar Cipher(+3)":
        plaintext = textFileList
        lastWord = plaintext[len(plaintext) -1]
        for word in plaintext:
            cipherText = ""
            alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
            plaintextPosition = 0
            while plaintextPosition < len(word):
                plaintextChar = word[plaintextPosition]
                alphabetPosition = 3
                while plaintextChar != alphabet[alphabetPosition]:
                    alphabetPosition = alphabetPosition + 1
                alphabetPosition = alphabetPosition - 3
                cipherText = cipherText + alphabet[alphabetPosition]
                plaintextPosition = plaintextPosition + 1
            if cipherText == lastWord:
                decyptedText = decyptedText + cipherText
            else:
                decyptedText = decyptedText + cipherText + " "

    elif firstWord == "Morse Code":
        morseCodeDictionary = {
            ".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e",
            "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j",
            "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o",
            '.--.':"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t",
            "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y",
            "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4",
            ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9",
            "-----":"0", "/":" "
        }
        for character in textFileList:
            decyptedText = decyptedText + morseCodeDictionary[character]

    newFile = open(os.path.join(sys.argv[2],file[0:len(file) - 4] + "_s55264aa.txt"),"w")
    newFile.write(decyptedText.lower())
    newFile.close()