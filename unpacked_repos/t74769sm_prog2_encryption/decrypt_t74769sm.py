import argparse
import os

parser = argparse.ArgumentParser(description='Get locations')
parser.add_argument('inputlocation', type=str)
parser.add_argument('outputlocation', type=str)
args = parser.parse_args()


def getdata(location):
    f = open(location, 'r')
    text = f.read()
    return text

def findAlg(stringsc):
    algtype = ""
    rem = 0
    for i in range(len(stringsc)):
        if stringsc[i] == ':':
            rem = i + 1
            break
        algtype += stringsc[i]
    decryptcode = ""
    while rem < len(stringsc):
        decryptcode += stringsc[rem]
        rem += 1
    if algtype == "Hex":
        return hexadeci(decryptcode)
    if algtype == "Caesar Cipher(+3)":
        return caesar3(decryptcode)
    if algtype == "Morse Code":
        return morseCode(decryptcode)


def morseCode(stringsc):
    character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    mcode = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
             '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-',
             '.....', '-....', '--...', '---..', '----.', '-----', '/']
    retrwrd = ""
    stringsc = stringsc.split()
    for x in stringsc:
        for y in range(len(mcode)):
            if x == mcode[y]:
                retrwrd += character[y]
    return retrwrd


def caesar3(stringsc):
    alph = "abcdefghijklmnopqrstuvwxyz"
    retrwrd = ""
    for i in range(len(stringsc)):
        temp = stringsc[i]
        if temp in alph:
            for j in range(len(alph)):
                if alph[j] == stringsc[i]:
                    tempj = j
                    tempj -= 3
                    if tempj < 0:
                        tempj += len(alph)
                    temp = alph[tempj]
        retrwrd += temp
    return retrwrd


def hexadeci(stringsc):
    retwrd = bytearray.fromhex(stringsc).decode()
    return retwrd


def writeFile(location, result):
    f = open(location, 'w')
    f.write(result)
    f.close()


fileLocation = args.inputlocation
outputFileLocation = args.outputlocation
lst = os.listdir(fileLocation)
for name in lst:
    newloc = fileLocation + '/' + name
    cipherWord = getdata(newloc)
    answer = findAlg(cipherWord)
    newout = outputFileLocation + '/' + name
    newout = newout.replace(".txt", "_t74769sm.txt")
    writeFile(newout, answer)