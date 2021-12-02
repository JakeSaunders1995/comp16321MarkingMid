import codecs
import argparse
from argparse import ArgumentParser
import os

def validateFilePath(f):
    if not os.path.exists(f):
        raise argparse.ArgumentTypeError("The filepath {0} does not exist. Please enter a valid filepath".format(f))
    return f

#hi
#COMMAND LINE INPUT
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument('inpFold', type=str, help="Input file/test txt file path")
parser.add_argument('outFold', type=str, help="Output file/output txt path")
args = parser.parse_args()
validateFilePath(args.inpFold)
validateFilePath(args.outFold)
inpFile=""

for filename in os.listdir(args.inpFold):#Get the amount of files within the folder
    if filename.endswith(".txt"):#that are input files
        
        inpFile=(os.path.join(args.inpFold, filename))
        filename=filename[:-4]+"_r61875lj.txt"
        outFile=(os.path.join(args.outFold, filename))
        
        inputFile = open(inpFile, "rt")
        algorithm = 0
        cipherText = ""
        caesarShift = ""
        plainText = ""
        currentMorseCode = ""
        morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morseNumber = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
        #morsePunctuation = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
        morsePunctuation =	{
          ".-.-.-": ".",
          "..--..": "?",
          "-.-.--": "!",
          "--..--": ",",
          "---...": ":",
          "-.-.-.": ";",
          "-.-.--": "!",
          "-....-": "-",
          "-.--.": "(",
          "-.--.-": ")",
          ".----.": "'",
          ".-..-.": "\"",
        }

        char = inputFile.read(1)
        if (char=="H"):
            algorithm=0
        elif (char=="M"):
            algorithm=1
        elif (char=="C"):
            algorithm=2
            while(char!="("):
                char=inputFile.read(1)
            while(char!=")"):
                char=inputFile.read(1)
                if(char!=")"): caesarShift+=char
            caesarShift=-int(caesarShift)
        else:
            print("Please enter a valid input file! formatted as: ALGORITHM:CIPHERTEXT")

        while(char!=":"):
            char=inputFile.read(1)
        cipherText = str(inputFile.read())
        #print(algorithm, cipherText)
        #print()

        if algorithm==0:#HEX CODE
            plainText = bytearray.fromhex(cipherText).decode()
            
        elif algorithm==1:#MORSE CODE
            for i in range(len(cipherText)):
                if(i==len(cipherText)-1):#if at the end
                    currentMorseCode+=cipherText[i]
                    notFound=True
                    for j in range(len(morseAlphabet)):
                        if(currentMorseCode==morseAlphabet[j]):
                            plainText+=chr(j+97)
                            notFound=False
                    for k in range(len(morseNumber)):
                        if(currentMorseCode==morseNumber[k]):
                            plainText+=str(k)
                            notFound=False
                    if(notFound):
                        if(currentMorseCode in morsePunctuation):
                            print("AAAA")
                            plainText+=morsePunctuation[currentMorseCode]
                            
                    currentMorseCode=""
                if(cipherText[i]==" "):#if finished word
                    notFound=True
                    for j in range(len(morseAlphabet)):
                        if(currentMorseCode==morseAlphabet[j]):
                            plainText+=chr(j+97)
                            notFound=False
                    for k in range(len(morseNumber)):
                        if(currentMorseCode==morseNumber[k]):
                            plainText+=str(k)
                            notFound=False
                    if(notFound):
                        if(currentMorseCode in morsePunctuation):
                            print("AAAA")
                            plainText+=morsePunctuation[currentMorseCode]
                    
                    currentMorseCode=""
                elif(cipherText[i]!=" " and cipherText[i]!="/"):#if not a space then add current character to current morse code
                    currentMorseCode+=cipherText[i]
                elif(cipherText[i]=="/"):#add space
                    plainText+=" "
                    
        elif algorithm==2:#CAESAR CODE
            for i in range(len(cipherText)):
                char=32
                if(ord(cipherText[i])<65 or (ord(cipherText[i])>90 and ord(cipherText[i])<97) or ord(cipherText[i])>122):
                        plainText+=cipherText[i]
                else:
                    char=ord(cipherText[i])+caesarShift;
                    if(char>122):char-=26
                    elif(char<97 and char>90):char+=26
                    elif(char>90 and char<97):char-=26
                    elif(char<65):char+=26
                    plainText+=chr(char)
                #print(cipherText[i],ord(cipherText[i]),ord(cipherText[i])+caesarShift,chr(char))
        
        outputText = open(outFile, "w")
        outputText.writelines(plainText)
        outputText.close()
