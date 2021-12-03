import argparse
import os

def solveMorseCode(cipherText):
    lookupTable = {
        '.-' : 'a',
        '-...' : 'b',
        '-.-.' : 'c',
        '-..' : 'd',
        '.' : 'e',
        '..-.' : 'f',
        '--.' : 'g',
        '....' : 'h',
        '..' : 'i',
        '.---' : 'j',
        '-.-' : 'k',
        '.-..' : 'l',
        '--' : 'm',
        '-.' : 'n',
        '---' : 'o',
        '.--.' : 'p',
        '--.-' : 'q',
        '.-.' : 'r',
        '...' : 's',
        '-' : 't',
        '..-' : 'u',
        '...-' : 'v',
        '.--' : 'w',
        '-..-' : 'x',
        '-.--' : 'y',
        '--..' : 'z',
        '.----' : '1',
        '..---' : '2',
        '...--' : '3',
        '....-' : '4',
        '.....' : '5',
        '-....' : '6',
        '--...' : '7',
        '---..' : '8',
        '----.' : '9',
        '-----' : '0',
        '.-.-.-': '.',
        '--..--': ',',
        '..--..': '?',
        '---...': ':',
        '-..-.': '/',
        '-....-': '-',
        '-...-': '=',
        '.----.': "'",
        '..--.-': '_',
        '-.-.--': '!',
        '.-...': '&',
        '.-..-.': '"',
        '-.-.-.': ';',
        '...-..-': '$',
        '/' : ' ',
    }

    plainText = ''
    listOfChars = cipherText.split(' ')

    for char in listOfChars:
        plainText += lookupTable.get(char)
    return plainText

def solveCaesar(cipherText):
    plainText = ''
    for char in cipherText:
        if (char == ' '):
            plainText += ' '
            continue
        
        # Convert to lower case
        char = char.lower()

        charToInt = ord(char)
        charToInt -= 3

        # Handle wrap around edge case for letters
        if (charToInt < 97 and charToInt > 94):
            charToInt += 26
        elif (charToInt < 48):
            charToInt += 10

        plainText += chr(charToInt)
    return plainText

def solveHexadecimal(cipherText):
    listOfChars = cipherText.split(' ')
    plainText = ''    
    for char in listOfChars:
        plainText += chr(int(char, 16))
    plainText = plainText.lower()
    return plainText
    
# Sort out parsing from command line and get the necessary file paths
parser = argparse.ArgumentParser(description='Decrypt cipher text')
parser.add_argument('inFolder', type=str, help='Path of folder containing cipher text')
parser.add_argument('outFolder', type=str, help='Path of folder to store the decrypted text')
args = parser.parse_args()
inFolderpath = args.inFolder
outFolderpath = args.outFolder

if (inFolderpath[0:-1] != "/"):
        inFolderpath += "/"

if (outFolderpath[0:-1] != "/"):
        outFolderpath += "/"

for filename in os.listdir(inFolderpath):
    
    inFileHandle = open(inFolderpath + filename, 'r')
    fullString = inFileHandle.readline()
    inFileHandle.close()

    # Split into type specifier and ciphertext
    splitString = fullString.split(':')
    inputType = splitString[0].strip('\n')
    cipherText = splitString[1].strip('\n')
    plainText = ''

    morseCodeID = 'Morse Code'
    caesarCipherID = 'Caesar Cipher(+3)'
    hexadecimalID = 'Hex'

    # Solve
    if (inputType == morseCodeID):
        plainText = solveMorseCode(cipherText)
    elif (inputType == caesarCipherID):
        plainText = solveCaesar(cipherText)
    elif (inputType == hexadecimalID):
        plainText = solveHexadecimal(cipherText)

    outputFileName = filename[0:len(filename) - 4] + "_h89565jc.txt"
    outFileHandle = open(outFolderpath + outputFileName, 'w')
    outFileHandle.write(plainText)
    outFileHandle.close()