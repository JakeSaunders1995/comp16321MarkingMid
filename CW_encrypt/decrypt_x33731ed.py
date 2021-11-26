import os
import sys
def getFiles():
    basepath = sys.argv[1]
    files = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            files.append(entry)
    return files

def outputFiles(output, filename):
    filename = filename[:len(filename)-4]
    f=open(sys.argv[2]+"\\"+filename+"_x33731ed.txt", "w+")
    f.write(output)
    f.close

def MorseCode(cipherText):
    Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----.",".-.-.-","..--..","-.-.--","--..--","---...","-.-.-.","-....-","-.--.","-.--.-",".----.",".-..-."]
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9",".","?","!",",",":",";","-","(",")","'","\""]
    plaintext = ""
    spaces = [-1]
    length = len(cipherText)
    for i in range(length):
        if(cipherText[i]==" "):
            spaces.append(i)
    spaces.append(length)
    for i in range(len(spaces)-1):
        morsechar = cipherText[spaces[i]+1:spaces[i+1]]
        if(morsechar != "/"):
            pos = Morse.index(morsechar)
            char = Alphabet[pos]
            plaintext += char
        else:
            plaintext += " "
    return plaintext
    
def Hex(cipherText):
    plaintext = ""
    length = len(cipherText) + 1
    for i in range(int(length/3)):
        hexnum = cipherText[i*3:i*3+2]
        decnum = int(hexnum, 16)
        character = chr(decnum)
        plaintext += character
    plaintext = plaintext.lower()
    return plaintext
    
def Caeser(cipherText):
    plaintext = ""
    length = len(cipherText)
    for i in range(length):
        if(cipherText[i]!=" "):
            asc = ord(cipherText[i])
            asc -= 3
            if(asc < 65):
                dif = 64-asc
                asc = 90-dif
            elif(asc < 97):
                dif = 96-asc
                asc = 122-dif
            char = chr(asc)
            plaintext += char 
        else:
            plaintext += cipherText[i]
    plaintext = plaintext.lower()
    return plaintext

def decrypt(inp):
    length= len(inp)
    colonPos = inp.find(":")
    if(colonPos==3):
        return Hex(inp[colonPos+1:length])
    elif(colonPos==10):
        return MorseCode(inp[colonPos+1:length])
    else:
        return Caeser(inp[colonPos+1:length])

files = getFiles()
for i in files:
    f = open(sys.argv[1]+"\\"+i,"r")
    inp = f.read()
    outputFiles(decrypt(inp), i)
    f.close()
print("done :)")

