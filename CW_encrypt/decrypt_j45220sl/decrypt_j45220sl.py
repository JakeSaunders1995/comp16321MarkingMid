import argparse
# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('inputfile', action='store', type=str)
parser.add_argument('outputfile', action='store', type=str)
args = parser.parse_args()
inputfile = args.inputfile
outputfile = args.outputfile
# read input
with open(inputfile, 'r') as FILE:
    string = FILE.readline()


def algorithm_morseCode(input):
    dict_moreseCode = {'a': '.-',
                       'b': '-...',
                       'c': '-.-.',
                       'd': '-..',
                       'e': '.',
                       'f': '..-.',
                       'g': '--.',
                       'h': '....',
                       'i': '..',
                       'j': '.---',
                       'k': '-.-',
                       'l': '.-..',
                       'm': '--',
                       'n': '-.',
                       'o': '---',
                       'p': '.--.',
                       'q': '--.-',
                       'r': '.-.',
                       's': '...',
                       't': '-',
                       'u': '..-',
                       'v': '...-',
                       'w': '.--',
                       'x': '-..-',
                       'y': '-.--',
                       'z': '--..'}

    input += ' '
    result = ''
    rawWord = ''
    for rawChar in input:
        if (rawChar != ' '):
            i = 0
            rawWord += rawChar
        else:
            i += 1
            if i == 2:
                result += ' '  # seperate word
            else:
                charIdx = list(dict_moreseCode.values()).index(rawWord)
                result += list(dict_moreseCode.keys())[charIdx]
                rawWord = ''
    return result


def algorithm_hex(input):
    rawChars = input.split()
    chars = [bytes.fromhex(char).decode('utf-8') for char in rawChars]
    result = ''.join(chars)
    return result


def algorithm_caesarplus3(input):
    plainText = ""
    for char in input:
        if char == ' ':
            plainText = plainText + char
            continue
        idx = ord(char) - ord("a")
        idxNew = (idx - 3) % 26  # shift = 3
        newchar = chr(idxNew + ord("a"))
        plainText = plainText + newchar
    return plainText


algorithm = string.split(':')[0]
ciphertext = string.split(':')[1].strip()
if algorithm == 'Morse Code':
    result = algorithm_morseCode(ciphertext.replace('/', ''))
elif algorithm == 'Hex':
    result = algorithm_hex(ciphertext)
else:
    result = algorithm_caesarplus3(ciphertext)

# output
with open(outputfile, "w") as file:
    file.write(result)