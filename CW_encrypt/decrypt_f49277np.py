import sys
import os
import string
alphabet="xyzabcdefghijklmnopqrstuvwxyzabc"
morseAlphabet ={
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    " " : "/",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----"
    }

inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())

path = sys.argv[1]
filelist=[]
files=os.listdir(path)
for f in files:
        filelist.append(f)
for x in filelist:
        decoded=""
        file = open(str(path)+x, "r")
        cipher= file.read()
        file.close()
        position=cipher.find(':')
        cipherType=cipher[0:position]
#Hex
        if cipherType=="Hex":
            decoded= bytes.fromhex(cipher[4:len(cipher)]).decode('utf-8')


#Caesar
        elif cipherType=="Caesar Cipher(+3)":
            ciphertextPosition = 18
            while ciphertextPosition < (len(cipher)):
                Char = cipher[ciphertextPosition]
                if Char not in string.whitespace:
                    if Char not in string.punctuation:
                        alphabetPosition= 31
                        while Char != alphabet[alphabetPosition]:
                            alphabetPosition -= 1
                        alphabetPosition -= 3
                        decoded = decoded + alphabet[alphabetPosition]
                        ciphertextPosition +=1
                    else:
                        decoded = decoded + str(Char)
                        ciphertextPosition +=1
                else:
                    decoded = decoded + Char
                    ciphertextPosition +=1


#morse
        else:
            word=""
            letter=""
            ciphertextPosition = 11
            while ciphertextPosition < len(cipher):
                    Char = cipher[ciphertextPosition]
                    if Char != " ":
                            letter += Char
                            ciphertextPosition+=1
                    elif Char == " " and cipher[ciphertextPosition+1] !="/":
                        word+=inverseMorseAlphabet[letter]
                        ciphertextPosition+=1
                        letter=""
                    elif Char == " " and cipher[ciphertextPosition+1] =="/":
                       word+=inverseMorseAlphabet[letter]
                       letter=""
                       decoded=decoded+word+" "
                       word=""
                       ciphertextPosition+=3
            letter=letter.rstrip()
            word+=inverseMorseAlphabet[letter]
            decoded=decoded+word



        out= str(x)
        index = out.find('.txt')
        outfile = out[:index]+"_f49277np.txt"
        outpath = str(sys.argv[2])+outfile
        file = open(outpath, "x")
        file.write(decoded)
        file.close()
