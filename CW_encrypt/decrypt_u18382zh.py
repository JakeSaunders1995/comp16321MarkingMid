import argparse
import os
count1 = ""
count2 = ""
count3 = ""
letter_morse = {
             "a":".-", "b":"-...", "c":"-.-.", "d":"-..",
"e":".", "f":"..-.", "g":"--.",
"h":"....", "i":"..", "j":".---", "k":"-.-",
"l":".-..", "m":"--", "n":"-.",
"o":"---", "p":".--.", "q":"--.-",
"r":".-.", "s":"...", "t":"-",
"u":"..-", "v":"...-", "w":".--",
"x":"-..-", "y":"-.--", "z":"--..", ".":".-.-.-", "?":"..--..", ",":"--..--", ":":"---...", ";":"-.-.-.",
"!":"-.-.--", "-":"-....-", "'":".----.", "=":"-...-", "/": "-..-.", "_":"..--.-", "(": "-.--.", ")":"-.--.-",
"$": "...-..-", "&":".-...", "@": ".--.-.", "+": ".-.-.", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
"5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

def Caesar(file1):
    ciphertext = file1
    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertextPosition = 0
    while ciphertextPosition < len(ciphertext):
        ciphertextChar = ciphertext[ciphertextPosition]
        alphabetPosition = 0
        if ciphertextChar == " ":
            plaintext += " "
            ciphertextPosition = ciphertextPosition + 1
        elif ciphertextChar == "\n":
            ciphertextPosition = ciphertextPosition + 1
        else:
            while ciphertextChar != alphabet[alphabetPosition]:
                alphabetPosition = alphabetPosition + 1
            alphabetPosition = alphabetPosition - 3
            plaintext = plaintext + alphabet[alphabetPosition]
            ciphertextPosition = ciphertextPosition + 1
    return  plaintext
def Hex(file2):
    c = ""
    a = file2.split(" ")
    for b in a:
        if b != "\n":
            b = chr(int(b, 16))
            c = c + b
    return c
def Morse(file3):
    letter_morse = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
        "e": ".", "f": "..-.", "g": "--.",
        "h": "....", "i": "..", "j": ".---", "k": "-.-",
        "l": ".-..", "m": "--", "n": "-.",
        "o": "---", "p": ".--.", "q": "--.-",
        "r": ".-.", "s": "...", "t": "-",
        "u": "..-", "v": "...-", "w": ".--",
        "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", "?": "..--..", ",": "--..--", ":": "---...",
        ";": "-.-.-.",
        "!": "-.-.--", "-": "-....-", "'": ".----.", "=": "-...-", "/": "-..-.", "_": "..--.-", "(": "-.--.",
        ")": "-.--.-",
        "$": "...-..-", "&": ".-...", "@": ".--.-.", "+": ".-.-.", "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
    }
    h = ""
    d = file3.split(" ")
    for e in d:
        if e != "\n":
            if e == "/":
                h = h + " "
            else:
                x = list(letter_morse.keys())[list(letter_morse.values()).index(e)]
                h = h + x
    return h




parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()
path = args.input
line = args.output
test = os.listdir(path)
if path[-1] != "/":
    path += "/"
if line[-1] != "/":
    line += "/"

for x in test:
    result = 0
    file = open(path + x, "r")
    w = file.read()
    colon = w.index(":")
    if w[0:6] == "Caesar" or w[0:6] == "caesar":
        plaintext = Caesar(w[colon+1:])
    elif w[0:3] == "Hex" or w[0:3] == "hex":
        c = Hex(w[colon+1:])
    else:
        h = Morse(w[colon+1:])

    if w[0:6] == "Caesar" or w[0:6] == "caesar":
        result = plaintext
    elif w[0:3] == "Hex" or w[0:3] == "hex":
        result = c
    else:
        result = h

    q = x[0:-4]

    f = open(str(line) + str(q) + "_u18382zh.txt", "w")

    f.write(result.lower())
    f.close()
    file.close()
