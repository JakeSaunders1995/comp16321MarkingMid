import argparse
import os
import binascii


def readText(filePath):
    f = open(filePath,encoding = "utf-8")


    txt=f.readline()
    f.close()
    return txt
def hex2str(s):	
    import textwrap
    return "".join([chr(i) for i in [int(b,16) for b in s.split(' ')]])



MorseList = {
".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
"....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
"---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
"..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

"-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
"-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
"..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
"....": "H", ".--.-.": "@", ".-.-.": "+",
}


def morse(string):
    retS=""
    list1 = string.split("/")
    for i in range(0,len(list1)):
        ss=list1[i].strip().split(" ")
        for code in ss:
            retS+=MorseList.get(code)
        retS+=' '
    return retS.lower()

def caesar2str(s):
    retS=""
    for p in s:
        if "a" <= p <= "z":
            retS+=chr(ord("a")+(ord(p)-ord("a")-3)%26)
        elif "A" <= p <= "Z":
            retS+=chr(ord("A")+(ord(p)-ord("A")-3)%26)
        else:
            retS+=p
    return retS

    

def createFileWrite(path,words):
    f=open(path,'a')
    f.write(words)
    f.close()

parser = argparse.ArgumentParser(description = 'Path')
parser.add_argument('inputpath', type=str, help='input file path')
parser.add_argument('outputpath', type=str, help='output file path')
args = parser.parse_args()

InputPath = args.inputpath
OutputPath = args.outputpath


encrywords=readText(InputPath)
arr=encrywords.split(':')
decrywords=""
if arr[0]=="Hex":
    decrywords=hex2str(arr[1])
elif arr[0]=="Caesar Cipher(+3)":
    decrywords=caesar2str(arr[1])
else:
    decrywords=morse(arr[1])

print(decrywords)
createFileWrite(OutputPath,decrywords)
