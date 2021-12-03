
import sys
import re
import os

# Stating input files
inputFile = sys.argv[1]
outputFile = sys.argv[2]

listAlgorithm = []
listBinary = []

# Open input file and read lines
for file in os.listdir(inputFile):
    with open(os.path.join(inputFile, file), 'r') as algorithm:
        lineAlgorithm = algorithm.readlines()

    # Creating the line with ciphertext in Algorithm
    listAlgorithm.append(lineAlgorithm)
    stringAlgorithm = ''.join(str(i) for i in listAlgorithm)


    # HEXADECIMAL

    if len(re.findall("Hex", stringAlgorithm)) > 0:
        # Convert Hex to ASCII
        stringBinary_Hex = bytes.fromhex(stringAlgorithm[6:-2])
        stringASCII_Hex = stringBinary_Hex.decode("ASCII").lower()

        # Write result into output file
        outputTxt = str(os.path.splitext(file)[0]) + "_s29576tb" + str(os.path.splitext(file)[1])
        fullOutputTxt = os.path.join("output_2/" + outputTxt)
        with open(fullOutputTxt, 'w') as out:
            for lines in stringASCII_Hex:
                out.write(lines)


    # CAESAR CIPHER

    elif len(re.findall("Caesar", stringAlgorithm)) > 0:
        # Convert Caeser to ASCI
        stringBinary_Caesar = stringAlgorithm[20:-2]
        stringASCII_Caesar = ''
        getRidOf = "\\n"
        stringBinary_Caesar = stringBinary_Caesar.replace(getRidOf, "")

        for i in range(len(stringBinary_Caesar)):
            char = ord(stringBinary_Caesar[i]) 
            
            # Checks for space
            if char == 32:
                stringASCII_Caesar = stringASCII_Caesar[0:] + ' '
            elif char == 46:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '.'
            elif char == 63:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '?'
            elif char == 33:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '!'
            elif char == 44:
                stringASCII_Caesar = stringASCII_Caesar[0:] + ','
            elif char == 58:
                stringASCII_Caesar = stringASCII_Caesar[0:] + ':'   
            elif char == 59:
                stringASCII_Caesar = stringASCII_Caesar[0:] + ';'
            elif char == 45:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '-'
            elif char == 91:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '['
            elif char == 93:
                stringASCII_Caesar = stringASCII_Caesar[0:] + ']'
            elif char == 123:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '{'
            elif char == 125:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '}'
            elif char == 40:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '('
            elif char == 41:
                stringASCII_Caesar = stringASCII_Caesar[0:] + ')'
            elif char == 39:
                stringASCII_Caesar = stringASCII_Caesar[0:] + "'"
            elif char == 34:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '"'
            elif char and (char + 1) and (char + 2) == 46:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '...'
            elif char == 97:
                stringASCII_Caesar = stringASCII_Caesar[0:] + 'x'
            elif char == 98:
                stringASCII_Caesar = stringASCII_Caesar[0:] + 'y'
            elif char == 99:
                stringASCII_Caesar = stringASCII_Caesar[0:] + 'z'
            elif char == 8211:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '–' # en dash
            elif char == 8212:
                stringASCII_Caesar = stringASCII_Caesar[0:] + '—' # em dash
            else:
                newChar = chr(char - 3)
                stringASCII_Caesar = stringASCII_Caesar[0:] + newChar

        # Write result into output file
        outputTxt = str(os.path.splitext(file)[0]) + "_s29576tb" + str(os.path.splitext(file)[1])
        fullOutputTxt = os.path.join("output_2/" + outputTxt)
        with open(fullOutputTxt, 'w') as out:
            for lines in stringASCII_Caesar:
                out.write(lines)
            
        
    # MORSE CODE

    elif len(re.findall("Morse", stringAlgorithm)) > 0:
        # Creating dictionary for all possible numbers / letters
        dictofMorseCode = {
            ".-": "a", 
            "-...": "b",
            "-.-.": "c", 
            "-..": "d", 
            ".": "e",
            "..-.": "f", 
            "--.": "g",
            "....": "h",
            "..": "i", 
            ".---": "j", 
            "-.-": "k", 
            ".-..": "l",
            "--": "m",
            "-.": "n", 
            "---": "o", 
            ".--.": "p",
            "--.-": "q", 
            ".-.": "r", 
            "...": "s", 
            "-": "t", 
            "..-": "u", 
            "...-": "v",
            ".--": "w", 
            "-..-": "x", 
            "-.--": "y", 
            "--..": "z",
            "-----": "0",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9",
            ".-.-.-": ".",
            "..--..": '?',
            "-.--.-": ")",
            "-.--.": "(",
            "--..--": ",",
            "-.-.-.": ";",
            "---...": ":",
            "-....-": "-",
            ".----.": "'",
            ".-..-.": '"',
            "-.-.--": "!",

        }

        stringBinary_MorseCode = stringAlgorithm[13:-2]
        stringASCII_MorseCode = ''

        # Iterating through each 'letter' in Morse Code using .split() and converting it into English using dictionary
        for i in stringBinary_MorseCode.split():
            if i == '/':
                stringASCII_MorseCode = stringASCII_MorseCode[0:] + ' '
            elif i != ' ':
                stringASCII_MorseCode = stringASCII_MorseCode[0:] + dictofMorseCode[i]
            else:
                pass

        # Writing result into output file
        outputTxt = str(os.path.splitext(file)[0]) + "_s29576tb" + str(os.path.splitext(file)[1])
        fullOutputTxt = os.path.join("output_2/" + outputTxt)
        with open(fullOutputTxt, 'w') as out:
            for lines in stringASCII_MorseCode:
                out.write(lines)
    
    listAlgorithm = []
    listBinary = []

