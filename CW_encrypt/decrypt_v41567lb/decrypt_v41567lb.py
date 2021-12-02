import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument("inp", type=str)
parser.add_argument("out", type=str)
args=parser.parse_args()
dir1=getattr(args, "inp")
dir2=getattr(args, "out")



def hexa(code):
    plaintext=""
    code=code.replace("Hex:","")
    code=code.replace(" ","")
    code=list(code)
    for i in range(0, len(code), 2):
        hd=code[i]+code[i+1]
        val=int(hd, 16)
        plaintext=plaintext+str(chr(val))
    return plaintext.lower()
def caesar(code):
    plaintext=""
    code=code.replace("Caesar Cipher(+3):","")
    code=list(code)
    for i in range(0, len(code)):
        if code[i] != " ":
            plaintext=plaintext+str((chr(ord(code[i])-3)))
        else:
            plaintext=plaintext+" "
    return plaintext
def morse(code):
    plaintext=""
    code=code.replace("Morse Code:","")
    code=code.split()
    morsecode ={'.-':'a', '-...':'b',
                '-.-.':'c', '-..':'d', '.':'e',
                '..-.':'f', '--.':'g', '....':'h',
                '..':'i', '.---':'j', '-.-':'k',
                '.-..':'l', '--':'m', '-.':'n',
                '---':'o', '.--.':'p', '--.-':'q',
                '.-.':'r', '...':'s', '-':'t',
                '..-':'u', '...-':'v', '.--':'w',
                '-..-':'x', '-.--':'y', '--..':'z'}
    for i in range(0, len(code)):

        if code[i]=="/":
            plaintext=plaintext+" "
        else:
            plaintext=plaintext+str(morsecode.get(code[i]))
    return plaintext

for infile in os.listdir(dir1):
    file=open(dir1+"/"+infile,"r")
    cipher=file.read()
    file.close()
    result=""
    if list(cipher)[0] == "H" or list(cipher)[0]  == "h":
        result=hexa(cipher)
    elif list(cipher)[0]  == "C" or list(cipher)[0]  == "c":
        result=caesar(cipher)
    elif list(cipher)[0]  == "M" or list(cipher)[0]  == "m":
        result=morse(cipher)
    outname=infile.replace(".txt", "_v41567lb.txt")
    outp=open(dir2+"/"+outname,"w")
    outp.write(result)
    outp.close()
