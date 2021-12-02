import os
import sys
import binascii
import string

mor = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
       '-..': 'D',      '.': 'E',   '..-.': 'F',
         '-.': 'G',   '....': 'H',     '..': 'I',  
      '.---': 'J',    '-.-': 'K',   '.-..': 'L',
        '--': 'M',     '-.': 'N',    '---': 'O', 
      '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
       '...': 'S',      '-': 'T',    '..-': 'U', 
      '...-': 'V',    '.--': 'W',   '-..-': 'X',
      '-.--': 'Y',   '--..': 'Z',  '-----': '0', 
     '.----': '1',  '..---': '2',  '...--': '3',
     '....-': '4',  '.....': '5',  '-....': '6', 
     '--...': '7',  '---..': '8',  '----.': '9'}

directory = sys.argv[1]
outputdirectory = sys.argv[2]
for filename in os.listdir(directory):
    filepath = directory + "/" + filename
    textfile = open(filepath, "r")
    text = textfile.read()

    def hex (textfile):
        hext = text[4:]
        hextext = bytes.fromhex(hext)
        hextext = hextext.decode("ascii")
        return hextext.lower()

    def cipher_decrypt(textfile):

        key = 3
        decryption = ""
        text1 = text[18:]
        text1.lower()

        for c in text1:
            if c.isupper(): 
                cin = ord(c) - ord('A')
                cpos = (cin - key) % 26 + ord('A')
                co = chr(cpos)
                decryption += co
            elif c.islower(): 
                cin = ord(c) - ord('a') 
                cpos = (cin - key) % 26 + ord('a')
                co = chr(cpos)
                decryption += co
            elif c.isdigit():
                co = (int(c) - key) % 10
                decryption += str(co)
            else:
                decryption += c
        return decryption


    def from_morse(textfile):
        out = []
        letter = []
        j = -1
        text.upper()
        text2 = text[11:] + " "
        for i in (text2.split()):
            j += 1
            letter += [i.split('/')]
            for k in range(len(letter[j])):
                out += mor.get(letter[j][k], ' ')
        return "".join(out).lower()


    path = outputdirectory
    if not os.path.exists(path):
        os.makedirs(path)


    if (text[0] == "H"):
        outputfile = outputdirectory + "/" + filename[0:-4] + "_" + "y69004la" + ".txt"
        s = open(outputfile, "w")
        s.write(hex(textfile))
        s.close()

    if (text[0] == "C"):
        outputfile = outputdirectory + "/" + filename[0:-4] + "_" + "y69004la" + ".txt"
        s = open(outputfile, "w")
        s.write(cipher_decrypt(textfile))
        s.close()

    if (text[0] == "M"):
        outputfile = outputdirectory + "/" + filename[0:-4] + "_" + "y69004la" + ".txt"
        s = open(outputfile, "w")
        s.write(from_morse(textfile))
        s.close()


