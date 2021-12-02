import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

input_folder = args.input
output_folder = args.output


for file in os.listdir(input_folder):
    f = open(input_folder+"/"+file)
    input_file_read = f.read()

    counter = 0
    input_file_reformed = ''
    for letter in input_file_read:
        if letter == ":":
            input_file_reformed = input_file_read[counter + 1:]
        counter += 1

    result = ""
    test_file = input_file_read.upper()

    if test_file[0:1] == "C":
        cipherText = ""
        plaintextPosition = 0
        alphabetLetter = 'abcdefghijklmnopqrstuvwxyz'
        alphabetList = list(alphabetLetter)
        while plaintextPosition < len(input_file_reformed):
            plaintextChar = input_file_reformed.lower()[plaintextPosition]

            if plaintextChar == ' ':
                cipherText = cipherText + ' '
                plaintextPosition = plaintextPosition + 1
            elif plaintextChar in alphabetList:
                letterValue = alphabetLetter.index(plaintextChar)
                letterValue = (letterValue - 3)
                cipherText = cipherText + alphabetLetter[letterValue]
                plaintextPosition = plaintextPosition + 1
            elif plaintextChar == '\n':
                cipherText += '\n'
                plaintextPosition += 1
            else:
                plaintextPosition += 1
        result = cipherText

    if test_file[0:1] == "M":
        morse_code = {
            '..-.': 'F', '-..-': 'X',
            '.--.': 'P', '-': 'T', '..---': '2',
            '....-': '4', '-----': '0', '--...': '7',
            '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
            '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
            '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
            '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
            '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
            '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1', '/': ' ',
        }
        decrypted = ''
        counter = 0
        output = ""
        for code in input_file_reformed:
            counter += 1
            decrypted += code
            if code == ' ' or counter == len(input_file_reformed):
                decrypted = decrypted.replace(' ', '')
                for item in morse_code:
                    if decrypted == item:
                        output += morse_code.get(item, item)
                        decrypted = ''
        result = output.lower()

    if test_file[0:1] == "H":
        input_file_reformed = input_file_reformed.split(" ")
        for numbers in input_file_reformed:
            numbers_in_bytes = bytes.fromhex(numbers)
            result += numbers_in_bytes.decode("ASCII")

    output_name = os.path.join(output_folder, file.replace(".txt", "_p15748aa.txt"))
    output_file = open(output_name, "w")
    output_file.write(result)
    output_file.close()
