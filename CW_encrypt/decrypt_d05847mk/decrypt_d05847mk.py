import os
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("inp")
parser.add_argument("otp")
args=parser.parse_args()
inputpath=args.inp
outputpath=args.otp
Morse_Code={"A" : ".-",
            "B" : "-...",
            "C" : "-.-.",
            "D" : "-..",
            "E" : ".",
            "F" : "..-.",
            "G" : "--.",
            "H" : "....",
            "I" : "..",
            "J" : ".---",
            "K" : "-.-",
            "L" : ".-..",
            "M" : "--",
            "N" : "-.",
            "O" : "---",
            "P" : ".--.",
            "Q" : "--.-",
            "R" : ".-.",
            "S" : "...",
            "T" : "-",
            "U" : "..-",
            "V" : "...-",
            "W" : ".--",
            "X" : "-..-",
            "Y" : "-.--",
            "Z" : "--..",
            "0" : "-----",
            "1" : ".----",
            "2" : "..---",
            "3" : "...--",
            "4" : "....-",
            "5" : ".....",
            "6" : "-....",
            "7" : "--...",
            "8" : "---..",
            "9" : "----.",
            " " : "/",
            ":" : "--..--",
            "." : ".-.-.-",
            "/" : "-..-.",
            "?" : "..--..",
            "-" : "-....-",
            "(" : "-.--.",
            ")" : "-.--.-"}
os.chdir(inputpath)
arr=os.listdir()

def decryptHex():
    a=bytearray.fromhex(cipher).decode()
    return a.lower()

def decryptCaesar():
    a=""
    p=0
    while p < len(cipher):
        pc=cipher[p]
        if pc==" ":
            a+=" "
        elif pc=="a":
            a+="x"
        elif pc=="b":
            a+="y"
        elif pc=="c":
            a+="z"
        else:
            a+=chr(ord(pc)-3)
        p+=1
    return a.lower()

def decryptMorse():
    a=""
    lst=cipher.split()
    for l in lst:
        for ascii, morse in Morse_Code.items():
            if morse==l:
                a+=ascii
    return a.lower()

def output_hex():
    opfilename=inpfile.replace(".txt","")+"_d05847mk.txt"
    opcon=decryptHex()
    os.chdir(outputpath)
    with open(opfilename,"w") as f:
        f.write(opcon)
    os.chdir(inputpath)

def output_caesar():
    opfilename=inpfile.replace(".txt","")+"_d05847mk.txt"
    opcon=decryptCaesar()
    os.chdir(outputpath)
    with open(opfilename,"w") as f:
        f.write(opcon)
    os.chdir(inputpath)

def output_morse():
    opfilename=inpfile.replace(".txt","")+"_d05847mk.txt"
    opcon=decryptMorse()
    os.chdir(outputpath)
    with open(opfilename,"w") as f:
        f.write(opcon)
    os.chdir(inputpath)

for inpfile in arr:
    if inpfile.endswith(".txt"):
        file=open(inpfile,"r")
        for line in file:
            line=line.rstrip()
            if line[:3].lower()=="hex":
                j=line.find(":")
                cipher=line[j+1:]
                output_hex()
            elif line[:3].lower()=="cae":
                j=line.find(":")
                cipher=line[j+1:]
                output_caesar()
            elif line[:3].lower()=="mor":
                j=line.find(":")
                cipher=line[j+1:]
                output_morse()
