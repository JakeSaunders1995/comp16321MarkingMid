
import argparse
import os


parser = argparse.ArgumentParser()      #argument setup
parser.add_argument("inputs")
parser.add_argument("outputs")
args = parser.parse_args()
#arg2 = parser.parse_args()




pathIn = args.inputs                #accepts argument 1 and argument 2 and assigns them as the path to folder
pathOut = args.outputs
fileNames = os.listdir(pathIn)



morseCode = { 
    ".-":"a",
    "-...":"b",
    "-.-.":"c",
    "-..":"d",
    ".":"e",
    "..-.":"f",
    "--.":"g",
    "....":"h",
    "..":"i",
    ".---":"j",
    "-.-":"k",
    ".-..":"l",
    "--":"m",
    "-.":"n",
    "---":"o",
    ".--.":"p",
    "--.-":"q",
    ".-.":"r",
    "...":"s",
    "-":"t",
    "..-":"u",
    "...-":"v",
    ".--":"w",
    "-..-":"x",
    "-.--":"y",
    "--..":"z",
    "/":" ",
    "-----":"0",
    ".----":"1",
    "..---":"2",
    "...--":"3",
    "....-":"4",
    ".....":"5",
    "-....":"6",
    "--...":"7",
    "---..":"8",
    "----.":"9",
    ".----.":"'",
    "-.--.-":")",
    "-.--.":"(",
    "---...":":",
    "--..--":",",
    "-.-.--":"!",
    ".-.-.-":".",
    "-....-":"-",
    ".-..-.":"\"",
    "..--..":"?",
    "-..-.":"/",
    "-.-.-.":";",
}
'''
the period#, question mark#, exclamation point#, comma#, colon#, semicolon, 
dash#, hyphen, brackets, braces, parentheses#, apostrophe#,
quotation mark#, and ellipsis#?.
'''

    





def morse_code(cipher):
    cipher = cipher.split(" ")
    plainText = ""
    for i in cipher:
        try:
            plainText = plainText+morseCode[i]
        except:
            plainText = plainText+i
    

    return plainText


def caeser(cipher):
    cipher = cipher.lower()
    plainText = ""
    for i in cipher:
        asciiVal = ord(i)
        if asciiVal >= 97 and asciiVal <= 122:
            asciiVal -=3
            if asciiVal<97:
                asciiVal +=26
            letter = chr(asciiVal)
            plainText = plainText + letter
        else:
            plainText = plainText + i
    return plainText 
        

def hexadec(cipher):
    plainText  = ""
    cipher = cipher.split(" ")
    for i in cipher:
        letter = int(i,16)
        letter = chr(letter)
        plainText = plainText + letter
    plainText = plainText.lower()
    return plainText


for j in fileNames:

    textIn = pathIn+"/"+j
    file = open(textIn,"r")
    cipherText = file.read()
    file.close()
    #print(cipherText)

    if cipherText[0].upper() == "M":
        cipherText = cipherText.replace(cipherText[:11],"")
        plainText = morse_code(cipherText)
    elif cipherText[0].upper() == "C":
        cipherText = cipherText.replace(cipherText[:18],"")
        plainText = caeser(cipherText)
    elif cipherText[0].upper() == "H":
        cipherText = cipherText.upper()
        cipherText = cipherText.replace(cipherText[:4],"")
        plainText = hexadec(cipherText)
    else:
        print("invalid input")
        quit()

    #print(plainText)


    txtStripped = j.replace(".txt","")  #removes.txt from input file so username can be added
    textOut = pathOut +"/"+txtStripped+"_w60078be.txt"
    #print(textOut)
    file = open(textOut,"w")               
    file.write(plainText)
    file.close()







