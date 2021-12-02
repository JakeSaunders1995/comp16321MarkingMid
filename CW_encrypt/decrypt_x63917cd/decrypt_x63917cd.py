import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
inputFolder = args.input
outputFolder = args.output
fileList = os.listdir(inputFolder)
numberFiles = len(fileList)

for i in range(numberFiles):

    fileIn = open(inputFolder + "/" + fileList[i], "r")
    text = fileIn.readline().strip(" ")
    fileIn.close()

    type = str(text)
    partitionType = type.partition(':')
    type = partitionType[0]

    encrypted = text.partition(":")[2]
    decrypted = ""

    if (type == "Hex"):
    	decrypted = bytes.fromhex(encrypted).decode('utf-8')

    elif (type == "Caesar Cipher(+3)"):
    	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.?!,:;-()[]''""..."
    	for x in encrypted:

    	        if x in alphabet:
    	            pos = alphabet.find(x)
    	            newPos = (pos - 3) % 26
    	            newChar = alphabet[newPos]
    	            decrypted += newChar
    	        else:
    	            decrypted += x
 

    elif (type == "Morse Code"):
        alphabet = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 
                    'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', 
                    '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'/', '-':'-....-','(':'-.--.', ')':'-.--.-'}

        keyList = list(alphabet.keys())
        valueList = list(alphabet.values())      
        numSpaces = encrypted.count(" ")
        count = 0
        encrypted+=" "
        encrypted.split(" ")

        while (count<=numSpaces):

            position = valueList.index(encrypted.split(" ")[count])
            char = keyList[position]
            if (char != "/"):
                decrypted+=char

            else:
                decrypted+=" "
            count+=1
    
    decrypted = decrypted.lower()
    outputFolder +="/"
    fileName = fileList[i].replace(".txt", "") + "_x63917cd.txt"
    outputName = os.path.join(outputFolder, fileName)
    fileOut = open(outputName, "w")
    fileOut.write (decrypted)
    fileOut.close()