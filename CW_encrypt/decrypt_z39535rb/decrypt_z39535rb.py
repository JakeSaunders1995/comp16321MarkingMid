import argparse
import os

parser = argparse.ArgumentParser(description="file path")
parser.add_argument("inputFile", type=str, help="input file path")
parser.add_argument("outputFile", type=str, help="output file path")
args = parser.parse_args()

inputPath = args.inputFile
fileList = os.listdir(inputPath)
fileList.sort()

outputPath = args.outputFile

for file in fileList:
    with open(inputPath + '/' + file) as f:
        code = f.read()
        if code.startswith("Hex:"):
            word = code[4:]
            decode = ''.join(chr(int(i, 16)) for i in word.split())
            plainTextHex = decode
            with open(outputPath + '/' + file[:-4] + '_z39535rb.txt', 'w') as s:
                s.write(plainTextHex.lower())
            s.close()
        elif code.startswith("Caesar Cipher(+3):"):
            word = code[18:]

            plainTextCeasar = ""
            cyphertextPosition = 0

            while cyphertextPosition < len(word) - 1:
                cyphertextChar = word[cyphertextPosition]
                if ord(cyphertextChar) == 32:
                    plainTextCeasar += " "
                elif 97 <= ord(cyphertextChar) <= 99:
                    ASCIIValue = ord(cyphertextChar)
                    ASCIIValue += 23
                    plainTextCeasar += chr(ASCIIValue)
                else:
                    ASCIIValue = ord(cyphertextChar)
                    ASCIIValue -= 3
                    plainTextCeasar += chr(ASCIIValue)
                cyphertextPosition += 1
            with open(outputPath + '/' + file[:-4] + '_z39535rb.txt', 'w') as s:
                s.write(plainTextCeasar.lower())
            s.close()
        elif code.startswith("Morse Code:"):
            word = code[11:]
            MorseList = {
                ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
                "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n",
                "---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
                "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

                "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
                ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

                "/": " ",
            }

            splitCode = word.split(" ")

            Text = [MorseList[letter] for letter in splitCode]
            plainTextMorse = ''.join(Text).lower()
            with open(outputPath + '/' + file[:-4] + '_z39535rb.txt', 'w') as s:
                s.write(plainTextMorse.lower())
            s.close()
    f.close()
