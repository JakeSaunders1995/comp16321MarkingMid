import argparse
import os
import sys

#command-line argument parser
argp = argparse.ArgumentParser(description='Input a file of a cypher text')
argp.add_argument('Input', metavar='input_path', type=str,
                    help='input folder')
argp.add_argument('Output', metavar='output_path', type=str,
                    help='output folder')

args = argp.parse_args()
inputPath = args.Input
outputPath = args.Output

#check if file exists
if not os.path.isdir(inputPath):
    print("Input directory does not exist...")
    sys.exit()
elif not os.path.isdir(outputPath):
    print("Creating output directory")
    os.makedirs(outputPath)

#check type of encryption
def encryptCheck(fileContent):
    if "Hex:" in fileContent: return hexDecrypt(fileContent)
    elif "Caesar Cipher(+3):" in fileContent: return ccDecrypt(fileContent)
    elif "Morse Code:" in fileContent: return mcDecrypt(fileContent)
    else: print("File doesn't specify encoding")

#decrypt hex
def hexDecrypt(cypherText):
    return bytearray.fromhex(cypherText[4:]).decode()

#decrypt caesar cypher
def ccDecrypt(input):
    cypherText = input[18:]
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    ccalphabet = "defghijklmnopqrstuvwxyzabc "
    plainText = ""
    for letter in cypherText:
        plainText += alphabet[ccalphabet.find(letter)]
    return plainText

#decrypt morse
def mcDecrypt(input):
    morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M',
    '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '--..--': ', ',
    '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '.----.': "'", '---...': ':',
    '-.--.': '(', '-.--.-': ')', '-.-.--': '!', '.-..-.': '"', '/': ' '}
    cypherText = input[11:]
    plainText = ""
    cypherLetter = ""
    for letter in cypherText:
        if letter != " ":
            cypherLetter += letter
        else:
            plainText += morse[cypherLetter]
            cypherLetter = ""
    plainText += morse[cypherLetter]
    return plainText

def outputFormat(outputText, filePath):
    with open(filePath, 'w') as f:
        f.write(outputText)
    print("Output File Created at: {} \n".format(filePath))

#the starting procedure
files = os.listdir(inputPath)
for x in files:
    with open("{}/{}".format(inputPath, x), 'r') as f:
        decryptedText = encryptCheck(f.read()).lower()
        outputFormat(decryptedText, "{}/{}".format(outputPath, x))
