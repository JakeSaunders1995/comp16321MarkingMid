import os,sys
input_file = sys.argv[1]
output_file = sys.argv[2]


GetRealPathInput = os.path.realpath(input_file)
filelist = os.listdir(GetRealPathInput)

for item in filelist:

    OpenFiles = open(GetRealPathInput + "/" + item, 'r')
    readInputFile = OpenFiles.read()
    print(readInputFile)

    GetFileNameInput = os.path.basename(item)

    GetPath = os.path.realpath(output_file)

    textname = GetFileNameInput.replace(".txt","_j72446cx.txt")



    outputfile = open(os.path.join(GetPath, textname),"w")


    if "Caesar" in readInputFile:
        plaintext = readInputFile.replace("Caesar Cipher(+3):", "")
        plaintext = plaintext.strip("\n")


        cipherText =""
        alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
        plaintextPosition = 0


        while plaintextPosition < len(plaintext):

            plaintextChar = plaintext[plaintextPosition]
            alphabetposition = 3
            if plaintextChar == " ":
                plaintextPosition += 1
                cipherText = cipherText + " "

            else:
                while plaintextChar != alphabet[alphabetposition]:
                    alphabetposition += 1
                alphabetposition -= 3
                cipherText = cipherText + alphabet[alphabetposition]
                plaintextPosition += 1
        outputfile.write(cipherText)





    if "Hex" in readInputFile:
        plaintext = readInputFile.replace("Hex:","")
        if " " in plaintext:
             plaintext = plaintext.replace(" ",chr(32))
        if "Hex:" in plaintext:
            plaintext = plaintext.replace("Hex:","")
        plaintext.split(" ")
        cipherText = ""
        plaintextPosition1 = 0
        plaintextPosition2 = 2

        while (plaintextPosition2 <= len(plaintext)):
            plaintextChar = plaintext[plaintextPosition1:plaintextPosition2]
            plaintextChar = int(plaintextChar,16)

            cipherText = cipherText + chr(plaintextChar)
            plaintextPosition1 += 3
            plaintextPosition2 += 3


        outputfile.write(cipherText)

    if "Morse" in readInputFile:
        message = readInputFile.replace("Morse Code:","")
        message = message.rstrip("\n")
        Splitmessage = message.split(" ")

        Morsedictionary = {'.-': 'a',
                '-...': 'b',
                '-.-.': 'c',
                '-..':'d',
                '.':'e',
                '..-.':'f',
                '--.': 'g',
                '....': 'h',
                '..': 'i',
                '.---':'j',
                '-.-': 'k',
                '.-..': 'l',
                '--': 'm',
                '-.': 'n',
                '---': 'o',
                '.--.': 'p',
                '--.-': 'q',
                '.-.': 'r',
                '...': 's',
                '-': 't',
                '..-': 'u',
                '...-': 'v',
                '.--': 'w',
                '-..-': 'x',
                '-.--': 'y',
                '--..': 'z',
                '.----': '1',
                '..---': '2',
                '...--': '3',
                '....-': '4',
                '.....': '5',
                '-....': '6',
                '--...': '7',
                '---..': '8',
                '----.': '9',
                '-----': '0',
                '..--..': '?',
                '-..-.': '/',
                '-.--.-': '()',
                '-....-': '-',
                '.-.-.-': '.',
                '/':' ',
                '-·-·--':'!'
        }
        for element in Splitmessage:


            outputfile.write(Morsedictionary[element])

    OpenFiles.close()
    outputfile.close()
