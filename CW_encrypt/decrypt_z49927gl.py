#fixed
import os
import sys
from pathlib import Path
import ntpath


fin = sys.argv[1]
fout = sys.argv[2]

for fin in os.scandir(fin):
    f = open(fin.path, 'r')
    in_file = f.readline().strip()
    f.close()
    plaintext = ""
    #caesar encryption
    if in_file[0] == "C":
        ciphertextposition = 18
        while ciphertextposition < len(in_file):
            if(in_file[ciphertextposition] == " "):
                plaintext = plaintext + " "
                ciphertextposition = ciphertextposition + 1
            else:
                ciphertextchar = in_file[ciphertextposition]
                value = ord(ciphertextchar)
                value = value - 3
                plaintext = plaintext + chr(value)
                ciphertextposition = ciphertextposition + 1
        rez = plaintext.lower()
        out_file = Path(fin).stem + "_z49927gl.txt"
        out_file = os.path.join(fout, out_file)
        output = open(out_file, 'w+')
        output.write(str(rez))
        output.close()
    #hex encryption
    elif in_file[0] == "H":
        i = 4
        hex = ""
        while i < len(in_file):
            hex = hex + in_file[i] + in_file[i+1]
            i = i+3
        result = bytes.fromhex((lambda s: ("%s%s00" * (len(s)//2)) % tuple(s))(hex)).decode('utf-16-le')
        rez = result.lower()
        out_file = Path(fin).stem + "_z49927gl.txt"
        out_file = os.path.join(fout, out_file)
        output = open(out_file, 'w+')
        output.write(str(rez))
        output.close()
    #morse encryption
    elif in_file[0] == "M":
        i = 11
        alpha = 'abcdefghijklmnopqrstuvwxyz1234567890'
        decryption = ['.-','-...',
                     '-.-.', '-..', '.',
                     '..-.', '--.', '....',
                     '..', '.---', '-.-',
                     '.-..', '--', '-.',
                     '---', '.--.', '--.-',
                     '.-.', '...', '-',
                     '..-', '...-', '.--',
                     '-..-', '-.--', '--..', '.----', '..---', '...--',
                    '....-', '.....', '-....',
                    '--...', '---..', '----.',
                    '-----',]
        cin = ""
        for i in range(11,len(in_file)):
            cin = cin + in_file[i]
        text = cin.split(" ")
        l = len(text)
        for x in range (0,l):
            for y in range(0,36):
                if( text[x] == decryption[y]):
                    plaintext = plaintext + alpha[y]
        #count how much words
        slashes = 1
        spaces = 0
        g = 0
        #how many slashes
        for i in range (0,len(in_file)):
            if(in_file[i] == "/"):
                slashes = slashes + 1
        count = [0] * slashes

        for i in range(0,len(in_file)):
            if in_file[i] == " ":
                spaces = spaces + 1
            if in_file[i] == "/":
                count[g] = spaces
                g = g + 1
                spaces = 0

        plaintext_update = ""
        r = 0
        chars = 0
        for i in range(0,slashes):
            while r < (count[i]-1):
                plaintext_update = plaintext_update + plaintext[r + chars]
                r = r + 1
            if(i != (slashes - 1)):
                plaintext_update = plaintext_update + " "
            chars = chars + count[i] - 1
            i = i + 1
            r = 0
        #extract the last word
        for i in range(chars + 1,len(plaintext)):
            plaintext_update = plaintext_update + plaintext[i]
        rez = plaintext_update.lower()

        out_file = Path(fin).stem + "_z49927gl.txt"
        out_file = os.path.join(fout, out_file)
        output = open(out_file, 'w+')
        output.write(str(rez))
        output.close()
