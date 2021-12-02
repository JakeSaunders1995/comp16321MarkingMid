import argparse
import re
import os

docParse = argparse.ArgumentParser(description="InputFile")
docParse.add_argument('Path', metavar='input path', type=str, help='filepath to input')
docParse.add_argument('Path2', metavar='output path', type=str, help='filepath to output')
args = docParse.parse_args()


inputDir = args.Path
for file in os.listdir(args.Path):
    inputfile = open(args.Path +"/"+ file)
    input = inputfile.read()
    cypher = re.split("[:]", input)
    morseDictionary = { 'a':'.-', 'b':'-...','c':'-.-.', 'd':'-..', 'e':'.','f':'..-.', 'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-',
    'l':'.-..', 'm':'--', 'n':'-.','o':'---', 'p':'.--.', 'q':'--.-','r':'.-.', 's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--',
    'x':'-..-', 'y':'-.--', 'z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-',}

    filename = file[:-4]

    if cypher[0] == "Hex" or cypher[0] == "hexadecimal":
        decodedText = bytearray.fromhex(cypher[1]).decode()
        if not os.path.exists(args.Path2):
            outputDir = os.mkdir(args.Path2)
        outputfile = open(args.Path2 +"/"+filename+ "_f57695ks.txt", "w")
        decodedText = decodedText.lower()
        outputfile.write(decodedText)
        outputfile.close()
    elif cypher[0] == "Caesar Cipher(+3)" or cypher[0] == "caesar +3":
        wordlist = cypher[1].split()
        finalList = []
        for word in wordlist:
            cryptext = word
            plainText = ""
            alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
            cryptextPos = 0
            while cryptextPos < len(cryptext):
                cryptextChar = cryptext[cryptextPos]
                alphaPos = 3
                while cryptextChar != alphabet[alphaPos]:
                    alphaPos += 1
                alphaPos -= 3
                plainText += alphabet[alphaPos]
                cryptextPos += 1
            finalList.append(plainText)
        if not os.path.exists(args.Path2):
            outputDir = os.mkdir(args.Path2)
        outputfile = open(args.Path2 +"/"+filename+ "_f57695ks.txt", "w")
        outputfile.write(' '.join(finalList))
        outputfile.close()
    elif cypher[0] == "Morse Code" or cypher[0] == "morseCode":
        morseSplitted = re.split("[/]", cypher[1])
        sentence = []
        for morseWord in morseSplitted:
            morseLetters = morseWord.split()
            newWord = ''
            for letter in morseLetters:
                newLetter = list(morseDictionary.keys())[list(morseDictionary.values()).index(letter)]
                newWord += newLetter
            sentence.append(newWord)
        if not os.path.exists(args.Path2):
            outputDir = os.mkdir(args.Path2)
        outputfile = open(args.Path2 +"/"+filename+ "_f57695ks.txt", "w")
        outputfile.write(' '.join(sentence))
        outputfile.close()
