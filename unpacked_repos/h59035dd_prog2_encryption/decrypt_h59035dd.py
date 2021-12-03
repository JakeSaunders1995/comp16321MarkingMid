import os
import sys

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]
for file in os.listdir(inputFolder):#reads file from directory
    input = open(inputFolder + "/" + file, "r")
    data = input.read()
    i = 0
    encrypction = ""
    while data[i] != ":": #checks which coding is used
        encrypction += data[i]
        i += 1
    text = ""#decrypted text

    if(encrypction == "Hex"):#decrypts hex
        text = bytes.fromhex(data[i+1:len(data)]).decode("utf-8")
    elif(encrypction == "Morse Code"):#decyprts Morse Code
        letters = "abcdefghijklmnopqrstuvwxyz0123456789.?!,:;_-()'\"" #string of alphabet and punctuation
        morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", #list of codes, their location is same as characters they represent in string
         "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
         "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....",
         "--...", "-....", "---..", "----.", ".-.-.-", "..--..", "-.-.--", "--..--", "---...", "-.-.-.", "..--.-", "-....-", "-.--.", "-.--.-", ".----.", "", ".-..-."]
        symbol = ""
        i += 1
        while i < len(data):
            if (data[i] != " "):#checks if morse code character ended
                symbol += data[i]
            if (data[i] == " " or i == len(data) - 1):
                if(symbol == "/"):#detects places where you have to insert space
                    text += " "
                else:
                    for m in range(0,len(letters)):
                        if(symbol == morseCode[m]):
                            text += letters[m]#adds decoded character
                symbol = ""
            i += 1
            #print(symbol)
    elif(encrypction == "Caesar Cipher(+3)"):#decrypts Ceasar cipher
        letters ="xyzabcdefghijklmnopqrstuvwxyz" #alphabet in string
        for j in range(i+1,len(data)):
            letter = False#checks if caesar cipher was applied
            for k in range(3, len(letters)):#applies Caesar cipher
                if(data[j] == letters[k]):
                    text += letters[k-3]
                    letter = True
            if (not letter):#for punctuation and numbers
                text += data[j]
    if(os.path.isfile(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt")):
        output = open(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt", "w")
    else:
        output = open(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt", "x")
    output.write(text.lower())
    input.close()
    output.close()
