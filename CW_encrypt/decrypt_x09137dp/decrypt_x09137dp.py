import os
import sys
import glob

username = "x09137dp"

algorithm = ""
plainText = ""

caesarAlpha = "xyzabcdefghijklmnopqrstuvw"
morseDict = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e",
             "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j",
             "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o",
             ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t",
             "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y",
             "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4",
             ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9",
             "-----":"0"}

for file in glob.iglob(sys.argv[1] + "/**"):
    input = open(file, 'r') #Opens input file in read only mode
    while True:
        #Figures out what algorithm was used in encoding
        char = input.read(1).casefold()
        if char == ":" :
            break
        else:
            algorithm = algorithm + char

    cipher = input.read()

    if "morse" in algorithm:
        workingCipher = ""

        for a in cipher:
            if a == "/":
                #Adds whitespace when a "/" is read
                plainText = plainText + " "
            elif a == "." or a == "-":
                #Adds character to cipher for decoding
                workingCipher = workingCipher + a
            elif a == " " and workingCipher != "":
                #Decodes current bit of morse code and adds to plainText
                char = str(morseDict.get(workingCipher))
                plainText = plainText + char
                workingCipher = ""

        #Converts Last bit of morse code
        char = str(morseDict.get(workingCipher))
        plainText = plainText + char


    elif "caesar" in algorithm:
        for char in cipher:
            if char in caesarAlpha:
                currentPos = caesarAlpha.index(char)
                newPos = currentPos - 3
                plainText = plainText + caesarAlpha[newPos]
            elif char == " ":
                #Adds whitespace when a " " is read
                plainText = plainText + " "


    elif "hex" in algorithm:
        text = bytes.fromhex(cipher) #Changes hex to bytes
        text = text.decode("ascii") #Decodes bytes using the ASCII encoding
        plainText = plainText + text #Adds decoded text to plainText

    path, filenameExt = os.path.split(file)
    filename, extentsion = os.path.splitext(filenameExt)

    outputPath = os.path.join(sys.argv[2], filename + "_" + username + ".txt")
    output = open(outputPath, 'w') #Creates and opens output file in write mode
    output.write(plainText.lower())
    plainText = ""
    algorithm = ""

    output.close()
    input.close()
