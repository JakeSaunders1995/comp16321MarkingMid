import argparse
import os
#pathsetting
parser = argparse.ArgumentParser()
parser.add_argument('filepath1')
parser.add_argument('filepath2')
args = parser.parse_args()
inputpath = args.filepath1
outputpath = args.filepath2

#function setting
def separatedata (lines):
    algorithm = ""
    ciphertext = ""
    count = 1            
    for x in lines:
        if x == ":":
            ciphertext = lines[count:len(lines)]
            algorithm = lines[0:count-1]
            break
        else:
            count = count + 1
    return algorithm, ciphertext
   
def toHex(cipherlist):
    result=""
    current = ""
    for x in cipherlist:
        if x != " " and ord(x) != 10:
            current = current + str(x)
        else:
            if current != "":
                thisword = chr(int(current, 16))
                if ord(thisword) > 64 and ord(thisword) < 91:
                    thisword = thisword.lower()
                result = result + thisword
                current = ""
            if ord(x) == 10:
                result = result + "\n"
    if current !="":
        thisword = chr(int(current, 16))
        if ord(thisword) > 64 and ord(thisword) < 91:
            thisword = thisword.lower()
        result = result + chr(int(current, 16))
    return result

def toCaesar(cipherlist):
    result=""
    for x in cipherlist:
        for y in x:
            if ord(y) > 64 and ord(y) < 91:
                x = x.lower()
            if y == "c":
                current = "z"
            elif y == "b":
                current = "y"
            elif y == "a":
                current = "x"
            elif y == " ":
                current = " "
            elif ord(y) > 47 and ord(y) < 58:
                current = str(y)
            elif ord(y)==10:
                current = "\n"
            else:
                current = chr(ord(y)-3)
            result = result + current
        result = result
    return result  

def toMorse(cipherlist):
    result = ""
    current = ""
    Code = {
            'a': '.-',     'b': '-...',   'c': '-.-.',
            'd': '-..',    'e': '.',      'f': '..-.',
            'g': '--.',    'h': '....',   'i': '..',
            'j': '.---',   'k': '-.-',    'l': '.-..',
            'm': '--',     'n': '-.',     'o': '---',
            'p': '.--.',   'q': '--.-',   'r': '.-.',
            's': '...',    't': '-',      'u': '..-',
            'v': '...-',   'w': '.--',    'x': '-..-',
            'y': '-.--',   'z': '--..',
    
            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.', 

            '?': '..--..', '!': '-·-·--',
            '.': '.-.-.-', ',': '--..--',  
            '(': '-.--.',  ')': '-.--.-',
            ';': '-.-.-.', ':': '---...', 
            '-': '-....-', '—': '--..--', 
            '"': '.-..-.', "'": '.----.',  
        }
    for x in cipherlist:
        if x == "/":
            result = result + " "
        elif x == " " or ord(x) == 10:
            for k, v in Code.items():
                if v == current:
                    result = result + k
                    current = ""                   
        else:
            current = current + x
        if ord(x) == 10:
            result = result + "\n"
    for k, v in Code.items():
        if v == current:
            result = result + k
    return result

#input
inputfiles = os.listdir(inputpath)
os.chdir(inputpath)
for files in inputfiles: 
    plaintext = ""
    with open(files) as file:
    	lines = file.read()
    file.close()
    algo, cipher = separatedata(lines)
    if algo == "Hex":
        plaintext = toHex(cipher)
    elif algo == "Caesar Cipher(+3)":
        plaintext = toCaesar(cipher)
    elif algo == "Morse Code":
        plaintext = toMorse(cipher)    

#output
    filesname = str(files)
    name = filesname[0:-4] + "_m73289ls.txt"
    os.chdir(outputpath)
    with open(name, 'w') as file:
        file.write(plaintext)
    file.close()
    os.chdir(inputpath)
