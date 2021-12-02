import sys
print("argument list: ", str(sys.argv))

infile = sys.argv[1]
outfile = sys.argv[2]

infile = open(infile, "r")
fileString = infile.read()
x = fileString.split(":")
print(x)
algorithm = x[0]
cipherText = x[1]

#decryption dictionarys
hexDict = {

}
plainText = ""
if (algorithm == "Hex"):
    print("Hex")
    plainText = bytearray.fromhex(cipherText).decode()

elif(algorithm == "Caesar Cipher(+3)"):
    print("caeser cipher")
    print(list(cipherText))
    for i in range(len(list(cipherText))):
        if(cipherText[i] == " "):
            plainText += " "
        else:
            ASCIIval = ord(cipherText[i])
            print(ASCIIval)
            ASCIIval -= 3
            decodedChar = chr(ASCIIval)
            print(decodedChar)
            plainText += decodedChar
            print(plainText)



elif(algorithm == "Morse Code"):
    print("Morse Code")
    morseDict = {
        '.-': 'a',   '-...': 'b',   '-.-.': 'c',
        '-..': 'd',      '.': 'e',   '..-.': 'f',
        '--.': 'g',   '....': 'h',     '..': 'i',  
        '.---': 'j',    '-.-': 'k',   '.-..': 'l',
        '--': 'm',     '-.': 'n',    '---': 'o', 
        '.--.': 'p',   '--.-': 'q',    '.-.': 'r',
        '...': 's',      '-': 't',    '..-': 'u', 
        '...-': 'v',    '.--': 'w',   '-..-': 'x',
        '-.--': 'y',   '--..': 'z',  
        '-----': '0', 
        '.----': '1',  '..---': '2',  '...--': '3',
        '....-': '4',  '.....': '5',  '-....': '6', 
        '--...': '7',  '---..': '8',  '----.': '9',
        '.....':'.', '.-.-.-':',', '-.-.-.':';', 
        '---...':':', '..--..':'?', '--..--':'!'
    }

    morseChars = cipherText.split(" ")
    print(morseChars)

    for i in range(len(morseChars)):
        if morseChars[i] == "/":
            plainText += " "
        else:
            print(morseDict[morseChars[i]])
            plainText += morseDict[morseChars[i]]

        print(plainText)

print(plainText)

#write to output file
outOpen = open(outfile, "w")
outOpen.write(plainText)
outOpen.close()