import argparse
import os

parser = argparse.ArgumentParser(description="I/O file path")
parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")
args = parser.parse_args()


def Decrypt_morsecode(cipher):
    result = ""
    codelist = {
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
        "-.-.-": ".",
        "---...": ":",
        "--..--": ",",
        "-.-.-.": ";",
        "..--..": "?",
        "-...-": "=",
        ".----.": "'",
        "-..-.": "/",
        "-.-.--": "!",
        "-....-": "-",
        "..--.-": "_",
        ".-..-.": '"',
        "-.--.": "(",
        "-.--.-": ")",
        "...-..-": "$",
        ".--.-.": "@",
        ".-.-.": "+",
        "/": " "
    }
    cipherlist = cipher.split(" ")
    for word in cipherlist:
        result += codelist.get(word)
    return result


def Decrypt_hex(cipher):
    result = ""
    charlist = cipher.split(" ")
    for char in charlist:
        result += chr(int(char, 16))
    return result


def Decrypt_caesar(cipher):
    result = ""
    for i in cipher:
        if i == " ":
            result += " "
            continue  # Append a space if i is space
        # There can be some special cases
        elif i == "a":
            result += "x"
            continue
        elif i == "b":
            result += "y"
            continue
        elif i == "c":
            result += "z"
            continue
        result += chr(ord(i) - 3)
    return result


for filename in os.listdir(args.input_folder_path):
    result = ""

    inputfile = open(f"{args.input_folder_path}/{filename}", "r")
    inputdata = inputfile.read().rstrip().split(":")
    inputfile.close()

    if inputdata[0] == "Caesar Cipher(+3)":
        result = Decrypt_caesar(inputdata[1])
    elif inputdata[0] == "Morse Code":
        result = Decrypt_morsecode(inputdata[1])
    elif inputdata[0] == "Hex":
        result = Decrypt_hex(inputdata[1])

    result = result.lower()  # Change everything to lower case

    outputfile = open(f"{args.output_folder_path}/{filename[:-4]}_j36001zl.txt", "w")
    outputfile.write(result)
    outputfile.close()
