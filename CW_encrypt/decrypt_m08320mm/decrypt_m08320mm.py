#--- Encryption ---
#takes input and output file as arguments
import argparse
import os
parser = argparse.ArgumentParser()
try:
    parser.add_argument('inputFile')
    parser.add_argument('outputFile')
    args = parser.parse_args()
except:
    print("List arguments in the form: python3 rugby_m08320mm.py [input file path] [output file path]")
    exit()

#Morse
def morseSwapper(morse):
    switcher = { #assigns each combination in morse code with the correct letter
        "/" : " ", ".-": "a", "-..." : "b", "-.-.": "c", "-.." : "d", ".": "e",
        "..-." : "f", "--.": "g", "...." : "h", "..": "i", ".---" : "j", "-.-": "k",
        ".-.." : "l", "--": "m", "-." : "n", "---": "o", "..--." : "p", "--.-": "q",
        ".-." : "r", "...": "s", "-" : "t", "..-": "u", "...-" : "v", ".--": "w",
        "-..-" : "x", "-.--": "y", "--.." : "z"
    }
    try: #in case of unexpected inputs
        return switcher[morse]
    except:
        return "(Null)"
def morseTextToList(morse):
    letter = str()
    allLetters = str()
    for i in range(len(morse)): #divides input text into characters using spaces
        if(morse[i]==" "):
            allLetters+=morseSwapper(letter)
            letter = str()
        elif morse[i]!="\n": #avoiding any new lines
            letter = letter + morse[i]
    allLetters+=morseSwapper(letter) #gets final character
    return allLetters

#Caesar
def shiftByThree(caeser):
    allLetters=str()
    ascii=0
    for i in range(len(caeser)):
        if(caeser[i]!="\n"): #avoids new lines
            ascii=ord(caeser[i])
            if(ascii>=97 and ascii<=122): #ASCII a=97,z=122
                ascii-=3
                if(ascii<97): #loops though lowercase alphabet range
                    ascii+=26
                allLetters+=chr(ascii)
            elif(ascii==32):
                allLetters+=" "
            else:
                allLetters+="(Null)" #in case of unexpected inputs
    return allLetters

#Hex
def hexToText(hex):
    letter = str()
    allLetters = str()
    for i in range(len(hex)): #divides input text into characters using spaces
        if(hex[i]==" "):
            allLetters+=chr(int(letter,base=16)).lower() #converts hex to decimal to character
            letter = str()
        elif hex[i]!="\n": #avoids new lines
            letter = letter + hex[i]
    allLetters+=chr(int(letter,base=16)) #adds final character
    return allLetters

def processFile(text):
    method = str()
    for i in range(len(text)): #splits code into
        if(text[i]==":"):
            method = text[0:i]
            code = text[i+1:]
            break
    #determines which decrytion to apply
    if(method=="Morse Code"):
        output = morseTextToList(code)
        print(output)
    elif(method=="Caesar Cipher(+3)"):
        output = shiftByThree(code)
        print(output)
    elif(method=="Hex"):
        output=hexToText(code)
        print(output)
    else:
        print("Unexpected information layout") #if file is not in the format expected
        exit()
    return output

#file handling
for file in os.listdir(args.inputFile):
    #checks if text file
    if file.endswith(".txt"):
        print("\n"+file)
        #reads file
        currentPath = os.path.join(args.inputFile, file)
        f = open(currentPath, "r")
        new = f.read()
        f.close()
        result = processFile(new)
        #writes to new file
        newPath = os.path.join(args.outputFile, file[0:-4]+"_m08320mm.txt")
        f = open(newPath, "w")
        f.write(result)
        f.close()
