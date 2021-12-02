import re
import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument("inputfolder")
parser.add_argument('outputfolder')

args=parser.parse_args()

inputfolder=args.inputfolder 
if(inputfolder[-1]!= '/'):
    inputfolder=inputfolder+'/'

outputfolder=args.outputfolder
if(outputfolder[-1]!='/'):
    outputfolder=outputfolder+'/'




input_files=os.listdir(inputfolder)

outputfile=os.listdir(outputfolder)



# print(outputfile)

def hex():
    hexM = encrypted
    bytes_object = bytes.fromhex(hexM)
    encmessage = bytes_object.decode("ASCII")
    encmessage=encmessage.lower()
    return encmessage

def caesar():
    text=encrypted
    text=text.lower()
    encmessage = ""
    textposition = 0

    while (textposition < len(text)):
        encChar = text[textposition]

        if (encChar == " "):
            encmessage +=" "

        else:
            if(encChar=='a'):
               encmessage += 'x'

            elif(encChar=='b'):
                encmessage += 'y'

            elif(encChar=='c'):
                encmessage += 'z'

            else:    
                ASCIIvalue = ord(encChar)
                ASCIIvalue = ASCIIvalue - 3
                encmessage = encmessage + chr(ASCIIvalue)

        textposition = textposition + 1  
    encmessage=encmessage[:-1]
    encmessage=encmessage.lower()
    return(encmessage)

def morse():

    morsedictionary ={'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ' ':'/' , '.':'.-.-.-' ,
                '?' :'..--..','!':'-.-.--' , ',': '--..--'
                , '{':'..--.', '}':'--..-', '...': '.-.-.-.-.-.-.-.-.-',
                 ':': '---...' , ';':'-....-','[':'.--...', ']':'-..---', '(' : '---...',  ')':'...---'
                , '-':'.---.', "'": '.----.' , '"':'.-..-.'}
                

    message = encrypted
    message += ' '
    encmessage = ''
    cyText = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            cyText += letter
        else:
            i += 1
            if i == 2:
                encmessage += ' '
            else:
                encmessage += list(morsedictionary.keys())[list(morsedictionary.values()).index(cyText)]
                cyText = ''
    encmessage=encmessage.lower()
    return encmessage

for file in range(len(input_files)):
    inputfile=open(inputfolder+input_files[file],'r')

    filecontents=inputfile.read()
    encryptedM=re.split(":",filecontents)
    binary=encryptedM[0]
    encrypted=encryptedM[1]


    if binary=='Hex':
        encmessage=hex() 

    elif binary=='Caesar Cipher(+3)':
        encmessage=caesar()
        
        
    elif binary=='Morse Code':
        encmessage=morse()
        
    

    outputfile=open(str(outputfolder)+str((input_files[file])[0:(len(input_files[file])-4)])+'_u60328el'+".txt",'w')
    outputfile.write(encmessage)





                                                                       













	
