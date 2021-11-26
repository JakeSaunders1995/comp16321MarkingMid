username = "_z54873hs.txt"
import sys
import os
LoadFile = sys.argv[1]
OutputFile = sys.argv[2]
for path , dir ,file in os.walk(LoadFile):
    Files = (file)


for j in Files:
    file = open(rf"{LoadFile}/{j}","r")
    file = file.read()    #
    if "Hex" in file:
        ciphertext= file

        new=ciphertext[4:]


        decoed = bytearray.fromhex(new)

        decoed= decoed.decode()

        decoed = decoed.lower()


        g = j.split(".")
        OutFile=open(f"{OutputFile}/{g[0]}{username}","w")

        OutFile.write(str(decoed))

        OutFile.close()


for j in Files:
    file = open(rf"{LoadFile}/{j}","r")
    file = file.read()    #
    if "Caesar" in file:

        cipherText = file
        cipherText= cipherText[18:]
        plainText= ""
        alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
        plaintextPosition = 0
        while plaintextPosition < len(cipherText):
            cipherTextChar = cipherText[plaintextPosition]
            alphabetPosition = 3
            if cipherTextChar not in alphabet:
                plainText = plainText + cipherTextChar
                plaintextPosition = plaintextPosition + 1
            else:


                while cipherTextChar != alphabet[alphabetPosition]:
                    alphabetPosition = alphabetPosition + 1
                alphabetPosition = alphabetPosition - 3
                plainText = plainText + alphabet[alphabetPosition]
                plaintextPosition = plaintextPosition + 1
        g = j.split(".")
        OutFile=open(f"{OutputFile}/{g[0]}{username}","w")

        OutFile.write(str(plainText))

        OutFile.close()


for j in Files:
    file = open(rf"{LoadFile}/{j}","r")
    file = file.read()
    file = file.strip()
    if "Morse Code" in file:

        morsesymbols =  {    'A':'.-', 'B':'-...',
                            'C':'-.-.', 'D':'-..', 'E':'.',
                            'F':'..-.', 'G':'--.', 'H':'....',
                            'I':'..', 'J':'.---', 'K':'-.-',
                            'L':'.-..', 'M':'--', 'N':'-.',
                            'O':'---', 'P':'.--.', 'Q':'--.-',
                            'R':'.-.', 'S':'...', 'T':'-',
                            'U':'..-', 'V':'...-', 'W':'.--',
                            'X':'-..-', 'Y':'-.--', 'Z':'--..',
                            '1':'.----', '2':'..---', '3':'...--',
                            '4':'....-', '5':'.....', '6':'-....',
                            '7':'--...', '8':'---..', '9':'----.',
                            '0':'-----', ', ':'--..--', '.':'.-.-.-',
                            '?':'..--..', '/':'-..-.', '-':'-....-',
                            '(':'-.--.', ')':'-.--.-' , " ": "/"}

        morsesymbols = {value: key for key, value in morsesymbols.items()}

        morsetext = file
        morsetext = morsetext[11:]
        morsepos = ""
        text=""

        for x in morsetext:
            if x != " ":
                morsepos=morsepos+x
            elif x == "/":
                text= text + " "
                #print(morsesymbols[morsepos], end= " ")
            else:

                text=text+(morsesymbols[morsepos])
                morsepos=""
        text=text+(morsesymbols[morsepos])
        morsepos=""

        g = j.split(".")
        OutFile=open(f"{OutputFile}/{g[0]}{username}","w")
        text= text.lower()

        OutFile.write(str(text))

        OutFile.close()
