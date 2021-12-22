import os, re, sys

hexDictionary = {
#numbers
    "30": "0",
    "31": "1",
    "32": "2",
    "33": "3",
    "34": "4",
    "35": "5",
    "36": "6",
    "37": "7",
    "38": "8",
    "39": "9",
#Characters
    "61": "a",
    "62": "b",
    "63": "c",
    "64": "d",
    "65": "e",
    "66": "f",
    "67": "g",
    "68": "h",
    "69": "i",
    "6a": "j",
    "6b": "k",
    "6c": "l",
    "6d": "m",
    "6e": "n",
    "6f": "o",
    "70": "p",
    "71": "q",
    "72": "r",
    "73": "s",
    "74": "t",
    "75": "u",
    "76": "v",
    "77": "w",
    "78": "x",
    "79": "y",
    "7a": "z",
    "20": " ",
#Capitals
    "41": "a",
    "42": "b",
    "43": "c",
    "44": "d",
    "45": "e",
    "46": "f",
    "47": "g",
    "48": "h",
    "49": "i",
    "4a": "j",
    "4b": "k",
    "4c": "l",
    "4d": "m",
    "4e": "n",
    "4f": "o",
    "50": "p",
    "51": "q",
    "52": "r",
    "53": "s",
    "54": "t",
    "55": "u",
    "75": "v",
    "57": "w",
    "58": "x",
    "59": "y",
    "5a": "z"
}

caesarDictionary = {
    "d": "a",
    "e": "b",
    "f": "c",
    "g": "d",
    "h": "e",
    "i": "f",
    "j": "g",
    "k": "h",
    "l": "i",
    "m": "j",
    "n": "k",
    "o": "l",
    "p": "m",
    "q": "n",
    "r": "o",
    "s": "p",
    "t": "q",
    "u": "r",
    "v": "s",
    "w": "t",
    "x": "u",
    "y": "v",
    "z": "w",
    "a": "x",
    "b": "y",
    "c": "z"
}

morseDictonary = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "/": " "
}







encryptions = os.listdir(sys.argv[1])

for i in range(len(encryptions)):
    currentCharacter= ""
    data = open(sys.argv[1] + '/' + encryptions[i])
    testHex =data.read(4)
    #print(fileType)
    if testHex == "Hex:":
        print("Hex")
        dataRead = ""
        wholeFile =data.read()
        data.close()
        data = open(sys.argv[1] + '/' + encryptions[i])
        testHex =data.read(4)
        hexLetter=""
        hexDecrpyt=""
        while dataRead != wholeFile:
            currentCharacter = data.read(1)
            if currentCharacter == " ":
                dataRead =  (dataRead + currentCharacter)
                hexLetter=""
                continue
            else:
                dataRead =  (dataRead + currentCharacter)
                hexLetter = (hexLetter + currentCharacter)
                if len(hexLetter)== 2:
                    hexDecrpyt = hexDecrpyt + hexDictionary[hexLetter]
        print(hexDecrpyt)
        hexDecryption = open(sys.argv[2] + "/" + str(i) + "_P2_q50676ep.txt" , "w")
        hexDecryption.write(hexDecrpyt)
        hexDecryption.close()
        data.close()



    elif testHex == "Caes":
        print("Caesar")
        currentCharacterCaes = ""
        dataRead = "ar Cipher(+3):"
        wholeFile =data.read()
        data.close()
        data = open(sys.argv[1] + '/' + encryptions[i])
        caesDecrpyt=""
        while currentCharacterCaes != ":":
            currentCharacterCaes = data.read(1)
        while dataRead != wholeFile:
            currentCharacterCaes = data.read(1)
            dataRead = dataRead + currentCharacterCaes
            if currentCharacterCaes == " ":
                caesDecrpyt= caesDecrpyt + " "
            elif currentCharacterCaes == "\n":
                continue
            elif currentCharacterCaes == "":
                continue
            else:
                caesDecrpyt= caesDecrpyt + caesarDictionary[currentCharacterCaes]
        print(caesDecrpyt)
        caesDecryption = open(sys.argv[2] + "/" + str(i) + "_P2_q50676ep.txt" , "w")
        caesDecryption.write(caesDecrpyt)
        caesDecryption.close()
        data.close()




    elif testHex == "Mors":
        print("Morse Code")
        currentCharacterMorse = ""
        dataRead = "e Code:"
        wholeFile =data.read()
        data.close()
        data = open(sys.argv[1] + '/' + encryptions[i])
        morse=""
        morseLetter=""
        while currentCharacterMorse != ":":
            currentCharacterMorse = data.read(1)
        while dataRead != wholeFile:
            currentCharacterMorse = data.read(1)
            dataRead = dataRead + currentCharacterMorse
            if currentCharacterMorse == " ":
                morse= morse + morseDictonary[morseLetter]
                morseLetter = ""
            elif currentCharacterMorse == "\n":
                continue
            elif currentCharacterMorse == "":
                continue
            else:
                morseLetter = morseLetter + currentCharacterMorse
        print(morse)
        morseDecryption = open(sys.argv[2] + "/" + str(i) + "_P2_q50676ep.txt" , "w")
        morseDecryption.write(morse)
        morseDecryption.close()
        data.close()



    else:
        print("Encryption not compatible.")
