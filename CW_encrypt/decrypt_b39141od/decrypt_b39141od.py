import sys
import os
files = os.listdir(sys.argv[1])
for file in files:

    f = open(os.path.join(sys.argv[1], file),'r')
    info = f.read().split(":")
    f.close()

    ciphertext = info[1]
    decoded = ""


    if info[0] == "Hex": #hex
        final = bytes.fromhex(ciphertext).decode('utf-8').lower()
    elif info[0] == "Caesar Cipher(+3)": #caesar
        final = ""
        for char in ciphertext:
            if char == " ":
                final += " "
                continue
            temp = ord(char.lower())
            temp -= 3
            if temp < ord('a'): #go back to end of alphabet if out of range
                temp += 26
            if chr(temp) in "abcdefghijklmnopqrstuvwxyz":
                final += chr(temp)
        decoded = final
    else: #morse code
        morseCodes = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-.-.-','--..--','..--..','-.-.--','.----.','-.--.','-.--.-','---...','-.-.-.','-....-']
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789.,?!'():;-"
        ciphertext = ciphertext.split(" ")
        final = ""
        for symb in ciphertext:
            if symb == "/":
                final += " "
                continue
            if symb in morseCodes:
                final += alphabet[morseCodes.index(symb)]

    decoded = final

    o = open(os.path.join(sys.argv[2], file[:-4]+"_b39141od.txt"),'w')
    o.write(decoded)
    o.close()
