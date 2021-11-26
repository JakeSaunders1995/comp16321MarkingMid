import os
import argparse



parser = argparse.ArgumentParser(description="decoder")
parser.add_argument('inp')
parser.add_argument('out')
args = parser.parse_args()


# HEX
def hex(code):
    return bytes.fromhex(code).decode("ASCII").lower()


punct = '''.?!,;:—-()[]{}...@#!$%^&*_+~—'"'''
# Caesar
def caesar(text):
    decoded = ""
    c = 0
    for x in text:
        if x in punct:
            decoded += x
        elif x.isdigit():
            decoded += x
        elif x.isspace():
            decoded += " "
        else:
            y = ord(x)-3.
            if y == 94:
                decoded += "x"
            elif y == 95:
                decoded += "y"
            elif y == 96:
                decoded += "z"
            else:
                decoded += chr(ord(x) - 3)
        c += 1
    return decoded.lower()


# MORSE

morsedict = {
    ".-":"A", "-...":"B", "-.-.":"C", "-..":"D",".":"E","..-.":"F","--.":"G", "....":"H","..":"I",".---":"J","-.-":"K",
    ".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",
    "/":" ",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0",
    ".-.-.-":".","..--..":"?","-.-.--":"!","--..--":",","-.-.-.":";","---...":":","-....-":"-","-.--.":"(","-.--.-":")",".-.-.- .-.-.- .-.-.-":"...",".--.-.":"@",
    ".----.":"'",".-..-.":'"'
}

def morse(code):
    msg = ""
    lst = code.split()
    for x in lst:
        if x not in morsedict.keys():
            continue
        else:
            msg += morsedict[x]
    return msg


def main(enc):
    enco = enc.split(":")
    chip = enco[1]
    key = enco[0]
    key = key.lower()
    if key in "hex":
        out = hex(chip)
        return out
    elif key in "caesar cipher(+3)":
        out = caesar(chip)
        return out
    elif key in "morse code":
        out = morse(chip)
        return out



dir = args.inp
spath = args.out

for file in os.listdir(dir):
    if file.endswith(".txt"):                   #iterates through input folder and executes the function on any .txt file
        ope= os.path.join(args.inp, file)
        r = open(ope, "r")
        content = r.read()
        y = main(content)
        fname = file.replace(".txt","")
        fname += "_y10240dt.txt"
        path = os.path.join(spath, fname)                       #write file on a specific path
        nf = open(path, "w")
        nf.write(y.lower())
        r.close()
        nf.close()
