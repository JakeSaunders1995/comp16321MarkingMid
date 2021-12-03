import os, argparse
from typing import Tuple
import string

# Dictionary representing the morse code chart (yes its on one line fight me)
MORSE_DICT = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', '/':' ', '.---':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9', '-----':'0', '.-.-.-':'.', '--..--':',', '---...':':', '..--..':'?', '.----.':"'", '-....-':'-', '-..-.':'/', '-.--.-':'()', '.-..-.':'"'}
USER_NAME = "j90095jb"

def ParseFile(path) -> Tuple[str, str]:
    file = open(path)
    data = file.readline()
    file.close()
    data = data.split(":", maxsplit= 1)
    return (data[0], data[1])

def WriteText(path, plaintext):
    file = open(path, "w")
    file.write(plaintext)
    file.close()

def GetAllFilesAtPath(dir) -> "list[str]":
    paths = []
    for path in os.listdir(dir):
        if path.endswith(".txt"):
            paths.append(os.path.join(dir, path))
    return paths

def GetOutputPath(path: str, outdir: str):
    return f"{os.path.join(outdir, os.path.splitext(os.path.basename(path))[0])}_{USER_NAME}.txt"

def DecodeMorse(cipher: str):
    plain = ""
    for code in cipher.split(" "):
        plain += MORSE_DICT[code]
    return plain
    
def DecodeCaeser(cipher: str):
    plain = ""
    for char in cipher:
        if char in string.ascii_lowercase:
            code = ord(char) - 3
            if code < 97: code += 26 # Looping within range of lowercase ASCII chars
            plain += chr(code)
    return plain
    
def DecodeHex(cipher: str):
    plaintext = ""
    chars = cipher.split(" ")
    for char in chars:
        plaintext += chr(int(char, base=16)).lower()
    return plaintext

def Main(inDir, outDir):
    for filename in GetAllFilesAtPath(inDir):
        dataIn = ParseFile(filename)
    
        if dataIn[0] == "Hex":
            plaintext = DecodeHex(dataIn[1])
        elif dataIn[0] == "Caesar Cipher(+3)":
            plaintext = DecodeCaeser(dataIn[1])
        elif dataIn[0] == "Morse Code":
            plaintext = DecodeMorse(dataIn[1])
        
        WriteText(GetOutputPath(filename, outDir), plaintext)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("Input")
    parser.add_argument("Output")
    args = parser.parse_args()
    Main(args.Input, args.Output)