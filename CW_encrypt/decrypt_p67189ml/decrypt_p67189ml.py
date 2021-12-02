import argparse
import re
import os

morse_chars = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "n",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
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
}


def decode_hex(ciphertext):
    spaces_removed = re.sub(" ", "", ciphertext)
    bytes_array = bytes.fromhex(spaces_removed)
    result = bytes_array.decode()
    return result


def decode_caesar(ciphertext):
    result = ""
    for char in ciphertext:
      code = ord(char)
      if 97 <= code <= 122:
        code -= 3
        if code < 97:
          code += 26
      result += chr(code)
    return result


def decode_morse(ciphertext):
    char_arr = ciphertext.split(" ")
    result = ""
    for char in char_arr:
        if char == "/":
            result += " "
        else:
            result += morse_chars[char]

    return result


parser = argparse.ArgumentParser()
parser.add_argument("inputDirectory")
parser.add_argument("outputDirectory")

args = parser.parse_args()

for filename in os.listdir(args.inputDirectory):
  filePath = os.path.join(args.inputDirectory,filename)
  if os.path.isfile(filePath):
    
    f = open(filePath, "r")
    string = f.read()
    f.close()

    algorithm = string[:string.find(":")]
    ciphertext = string[string.find(":")+1:].lower()

    output = ""
    if algorithm == "Hex":
      output = decode_hex(ciphertext)
    elif algorithm == "Caesar Cipher(+3)":
      output = decode_caesar(ciphertext)
    else:
      output = decode_morse(ciphertext)

    output = output.lower()

    f = open(args.outputDirectory + "/" + filename[:-4] + "_p67189ml.txt", "w")
    f.write(output)
    f.close()