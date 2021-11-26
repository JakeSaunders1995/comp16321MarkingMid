import sys
import os

def separateColon(textFile):
    textFile = textFile[2:-2]
    #separate at colon
    x = textFile.split(":")
    #lefthandside of colon = type of cipher
    separateColon.cipherType = x[0]
    #righthandside of colon = cipher text
    separateColon.cipherText = x[1]
    pass

def morse(decryptedText):
    morseCodeDict = {
        "a" :	".-",
        "b" :	"-...",
"c" :	"-.-.",
"d" :	"-..",
"e" :	".",
"f" :	"..-.",
"g" :	"--.",
"h" :	"....",
"i" :	"..",
"j" :	".---",
"k" :	"-.-",
"l" :	".-..",
"m"	 :"--",
"n"	: "-.",
"o"	:"---",
"p"	:".--.",
"q"	:"--.-",
"r"	:".-.",
"s"	:"...",
"t"	:"-",
"u"	:"..-",
"v"	:"...-",
"w"	:".--",
"x"	:"-..-",
"y"	:"-.--",
"z"	:"--..",	
"0"	:"-----",
"1"	:".----",
"2"	:"..---",
"3"	:"...--",
"4"	:"....-",
"5"	:".....",
"6"	:"-....",
"7"	:"--...",
"8"	:"---..",
"9"	:"----.",
"Error":	"........",
"&"	:".-...",
"'" 	:".----.",
"@" :".--.-.",
")" :	"-.--.-",
"(" :	"-.--.",
":" :	"---...",
"," :	"--..--",
"=" :"-...-",
"!"  :	"-.-.--",
"." :	".-.-.-",
"-"  :"-....-",
"+" :	".-.-.",
'"' :	".-..-.",
"?"	:"..--..",
"/" :"-..-."}


    words = separateColon.cipherText.split(" / ")
    for eachWord in words:
        letters = eachWord.split(" ")
        for letter in letters:
            #compare letter with dictionary
            #if letter in morseCodeDict.values() == True
                for key, value in morseCodeDict.items():
                    if letter == value:
                        decryptedletter = key
                        break
                decryptedText = decryptedText + decryptedletter         
                pass
        decryptedText += " "
    decryptedText = decryptedText[:-1] 
    return decryptedText
    pass

def hex(decryptedText):
    words = separateColon.cipherText.split(" ")
    for character in words:
        decryptedText = decryptedText + bytes.fromhex(character).decode('utf-8')
    return decryptedText

def caeser(decryptedText):
    caeserDict = {
"a" :	"d",
"b" :	"e",
"c" :	"f",
"d" :	"g",
"e" :	"h",
"f" :	"i",
"g" :	"j",
"h" :	"k",
"i" :	"l",
"j" :	"m",
"k" :	"n",
"l" :	"o",
"m"	 : "p",
"n"	: "q",
"o"	:"r",
"p"	:"s",
"q"	:"t",
"r"	:"u",
"s"	:"v",
"t"	:"w",
"u"	:"x",
"v"	:"y",
"w"	:"z",
"x"	:"a",
"y"	:"b",
"z"	:"c"}
    
    text = separateColon.cipherText.split(" ")
    for word in text:
        for letter in word:
            for key, value in caeserDict.items():
                if letter == value:
                   decryptedletter = key
                   break
            decryptedText = decryptedText + decryptedletter
            pass
        pass
        decryptedText += " "
    decryptedText = decryptedText[:-1] 
    return decryptedText
    pass

def createFolder():
    if os.path.exists(outFolder) == False:
        os.mkdir(outFolder)     
        createFolder.outputPath = os.path.abspath(outFolder)

def createTextFile():
    line = everyFile
    index = line.find(".txt")
    createTextFile.output_file = line[:index] + "_h52171rh" + ".txt"
    pass

def outputFileToFolder():
        completeName = os.path.join(outputPath, createTextFile.output_file)
        #create ouput file
        file1 = open(completeName, "w")
        file1.write(decryptedText)
        file1.close()

inFolder = sys.argv[1]
inFolderPath = os.path.abspath(inFolder)
outFolder = sys.argv[2]

#if outFolder already exists, quit program


if os.path.exists(outFolder) == False:
    os.mkdir(outFolder)     
    outputPath = os.path.abspath(outFolder)
else:
    outputPath = os.path.abspath(outFolder)

arr = os.listdir(inFolder)

for everyFile in arr:
    if os.getcwd() != inFolderPath:
        os.chdir(inFolderPath)
    
    decryptedText = ""
    with open(everyFile,'r') as i:
        textFile = str(i.readlines())
        separateColon(textFile)
        if separateColon.cipherType == "Morse Code":
            decryptedText = morse(decryptedText)
        elif separateColon.cipherType == "Caesar Cipher(+3)":
            decryptedText= (caeser(decryptedText))
        elif separateColon.cipherType == "Hex":
            decryptedText= (hex(decryptedText))
        createTextFile()
        outputFileToFolder()    
    pass