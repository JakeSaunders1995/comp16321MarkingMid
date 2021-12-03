import sys
import os
filles =[]
filles = os.listdir(str(sys.argv[1])) # Get all test files and put in list
morseDict = {'..-.': 'F', '-..-': 'X',
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C',
                  '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', 
                 '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3',
                  '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H',
                  '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', 
                 '-..': 'D',
                  '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U',
                  '.-': 'A',
                  '...': 'S', 
                 '.----': '1', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '}
for p in filles:
    if not p.startswith('.'):       #Ignores the hidden files
        fpath1 = str(sys.argv[1])
        fullname1 = os.path.join(fpath1,p)      #creates filepath for inputs
        fi1le = open(fullname1, encoding="utf8", errors='ignore')
        fpath = str(sys.argv[2])
        p = str(p)
        pos = int(p.find(".txt"))          
        fname = p[:pos] + "_q86352bb.txt"
        fullname = os.path.join(fpath,fname)       #creates the filename for the outouts 
        f = open(fullname, "w")        
        plaintext = ""
        letters =""
        morseletters =""
        for x in fi1le:
            ciphertext = str(x)
            pos = ciphertext.find(':')
            if x[0:pos] == "Morse Code":
                ciphertext = ciphertext[pos+1:]
                ciphertext += " "
                length = len(ciphertext)
                for y in range(0,length):
                    if ciphertext[y] == " " and y != 0:
                        plaintext += morseDict[morseletters]
                        morseletters = ""
                    else: 
                        morseletters += ciphertext[y]
            if x[0:pos] == "Caesar Cipher(+3)":
                ciphertext = ciphertext[pos+1:]
                ptextpos = 0
                while ptextpos < len(ciphertext):
                    if ciphertext[ptextpos] == " ":
                        plaintext += " "
                    else:
                        ptextchar = ciphertext[ptextpos]
                        asciival = ord(ptextchar) -3
                        plaintext += chr(asciival)
                    
                    ptextpos += 1
            if x[0:pos] == "Hex":
                ciphertext = ciphertext[pos+1:]
                length = len(ciphertext)
                n = 0
                while n < length:
                    if ciphertext[n] == " ":
                        p= 1
                    else:
                        let = bytes.fromhex(ciphertext[n:n+2]).decode('utf-8')
                        plaintext += let
                        p = 2
                    n+=p
        f.write(plaintext.lower())