import sys
import os

inputPath = sys.argv[1]
outputPath = sys.argv[2]

user = 'f85709jw'

def main ():
    for inp in os.listdir(inputPath):
        with open(inputPath + '/' + inp) as f:
            for line in f:
                algo, data = line.split(":")
                if algo[0] == "M":
                    output = morseCode(data)
                elif algo[0] == "H":
                    output = hexadecimal(data)
                elif algo[0] == "C":
                    output = caesarCypher(data)
                outputfile(output, inp)
                break

morseTranslate = {
    ".-" : "a",
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
    "/": " ",
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
    "--..--": ",",
    "..--..": "?",
    "-.-.--": "!",
    "---...": ":",
    "-....-": "-",
    ".----.": "'",
    ".-..-.": '"',
    "-.--.": "(",
    "-.--.-": ")",
}

def morseCode(data):
    morse = data.split(" ")
    answer =""
    for letter in morse:
        answer += morseTranslate[letter]
    return answer


def caesarCypher(data):
    letters = [chr(ord(x) - 3) if x != " " else x for x in data ]
    return "".join(letters)

def hexadecimal(data):
    encrhex = data.split(" ")
    answer = ""
    for letter in encrhex:
        answer += chr(int(letter,16)).lower()
    return answer

def outputfile(output, inputName):
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    with open(outputPath + '/' + inputName[0:-4] + '_' + user + '.txt', "w") as f:
        f.write(output)
    return

if __name__ == "__main__":
    main()