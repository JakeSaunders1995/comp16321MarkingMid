import argparse
import sys
import os
import string

filein = sys.argv[1]
fileout = sys.argv[2]

for filename in os.listdir(filein): 
    g = os.path.join(filein, filename)
    if os.path.isfile(g):
        filr = open(g, 'r')
        filen = os.path.basename(g)
        sfn = os.path.splitext(filen)[0]
    if os.path.isdir(fileout):
        dname = os.path.join(fileout, sfn + "_n20851ew.txt")
        fn = open(dname, 'w')
        text = filr.read()

        
        # CODE = {

        #         '.-':'a',
        #         '-...':'b',
        #         '-.-.':'c',
        #         '-..':'d',
        #         '.':'e',
        #         '..-.':'f',
        #         '--.':'g',
        #         '....':'h',
        #         '..':'i',
        #         '.---':'j', 
        #         '-.-':'k',
        #         '.-..':'l',
        #         '--':'m',
        #         '-.':'n',
        #         '---':'o',
        #         '.--.':'p',
        #         '--.-':'q',
        #         '.-.':'r',
        #         '...':'s',
        #         '-':'t',
        #         '..-.':'u',
        #         '...-':'v',
        #         '.--':'w',
        #         '-..-':'x',
        #         '-.--':'y',
        #         '--..':'z',
        #         '.----':'1',
        #         '..---':'2',
        #         '...--':'2',
        #         '....-':'4',
        #         '.....':'5',
        #         '-....':'6',
        #         '--...':'7',
        #         '---..':'8',
        #         '----.':'9',
        #         '-----':'0',
        #         '--..-- ':',', 
        #         '.-.-.-':'.',
        #         '..--..':'?',
        #         '-..-.':'?', 
        #         '-.--.':'(',
        #         '-.--.-':')' 
        #                         }

        CODE = { 'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--','_':'..--.-',  '0': '-----',  '1': '.----',  '2': '..---',
                '3': '...--',  '4': '....-',  '5': '.....',
                '6': '-....',  '7': '--...',  '8': '---..',
                '9': '----.' 
                }

                    

        if "Ceaser" in text:
            n = 17
            filr.seek(17)
            plainText = ''
            cipherText = text[n:]
            cipherTextPlace = 0
            while cipherTextPlace < len(cipherText):
                cipherTextCharacters = cipherText[cipherTextPlace]
                ASCIIval = ord(cipherTextCharacters)
                if ASCIIval == 32:
                    fn.write(" ")
                    cipherTextPlace +=1
                else:
                    ASCIIval = ASCIIval - 3
                    plainText = chr(ASCIIval)
                    fn.write(plainText)
                    cipherTextPlace +=1

        if "Hex" in text:
            n = 3
            filr.seek(n)
            while True:
                hexfile = filr.read(2)
                if not hexfile:
                    break
                string1 = bytes.fromhex(hexfile[0][4:])
                string1 = string1.decode('ascii')
                string1 = string1.lower()
                fn.write(string1)
                n += 3
        elif "Morse" in text:
            n = 9
            filr.seek(9)
            for line in filen:
                for combination in line.split():
                    if combination == '/':
                        fn.write(" ")
                    else:
                        combination = CODE[combination]
                        fn.write(combination)
    else:
        os.mkdir(fileout)