#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('inf')
parser.add_argument('outf')
args=parser.parse_args()

def binary(string):
    n=1<<7
    v=0
    out=""

    # runs through and gets a binary charicter seperated by a space
    for c in string:
        if c==' ':
            out+=chr(v)
            n=1<<7
            v=0
        else:
            v+=(ord(c)-48)*n
            n=n>>1
    out+=chr(v)
    return out

def hexcode(string):
    # dictionary of hex charicters and their values, defo a better way to do this
    chars = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
             'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    out = ""
    # loops through the string getting char values for each 2 hex values
    for i in range(0,len(string),3):
        v = 16*chars[string[i]] + chars[string[i+1]]
        out+=chr(v)
    return out

def morse(string):
    # Morse To Functional charicter
    string+=" "
    mtf = { '.-':'a', '-...':'b', '-.-.':"c", '-..':"d", '.':"e",
            '..-.':"f", '--.':"g", '....':"h", '..':"i", '.---':"j",  '-.-':"k",
            '.-..':"l", '--':"m", '-.':"n", '---':"o", '.--.':"p", '--.-':"q",
            '.-.':"r", '...':"s", '-':"t", '..-':"u", '...-':"v", '.--':"w",
            '-..-':"x", '-.--':"y", '--..':"z", "/":" "}
    out = ""
    morse=""
    # goes through getting morse seperated by spaces
    for c in string:
        if(c==" "):
            out+= mtf[morse]
            morse=""
        else:
            morse+=c
    return out
def ceaser(string):
    ret =""
    for c in string:
        if c!=" ":
            ret += chr(ord(c)-3)
        else:
            ret+=" "
    return ret

functions = {"Morse Code":morse,"Hex":hexcode,"binary":binary,"Caesar Cipher(+3)":ceaser}

path, dirs, files = next(os.walk(args.inf))

fileCount = files
print(path)
for i in files:
    ifile = path+"/" +i
    ofile = args.outf+ "/"+ i[0:-4] + "_k96010wp.txt"
    inp = open(ifile).read()
    i = 0
    # finding the colon, i know you can do it fast with regex but i didnt want to
    for c in range(len(inp)):
        if(inp[c]==":"):
            i=c
            break

    # it gets the decryption function from the dictionary above and jams the cipher text into it
    output = functions[inp[0:i]](inp[i+1:])

    outfile = open(ofile,"w")
    outfile.write(output)
    outfile.close()
