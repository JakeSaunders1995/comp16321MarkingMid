def hex(text):
    decryptedText = bytearray.fromhex(text).decode()
    return decryptedText

def caesar(text):
    decryptedText = ""
    words = text.split()
    for word in words:
        for i in word:
            ascii = ord(i) - 3
            if ascii < 97:
                ascii = ascii + 26
            decryptedText = decryptedText + chr(ascii)
        decryptedText = decryptedText + " "
    return decryptedText

def morse(text):
    morse = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0"}
    decryptedText =""
    words = text.split()
    for word in words:
        if word == "/":
            decryptedText = decryptedText + " "
        else:
            decryptedText = decryptedText + morse[word]
    return decryptedText

import argparse,os,re
parser = argparse.ArgumentParser(description="decrypts messages")
parser.add_argument("input", help="Input file path")
parser.add_argument("save",help="Output file path")
folder = parser.parse_args()
for filename in os.listdir(folder.input): 
    if filename.endswith(".txt"):
        inputFile = open(folder.input + filename,"r")
        outputFile = open(folder.save + filename[0:-4] + "_m31181jg" + ".txt","w") 
        text = inputFile.readline()
        encryptionType = ""
        for i in range(len(text)):
            if text[i] == ":":
                encryptionType = text[0:i+1]
                break
        if encryptionType =="Hex:":
            text = hex(text[i+1:len(text)])
        elif encryptionType =="Caesar Cipher(+3):":
            text = caesar(text[i+1:len(text)])
        elif encryptionType =="Morse Code:":
            text = morse(text[i+1:len(text)])
        text = text.lower()
        outputFile.write(text)
        outputFile.close
        inputFile.close