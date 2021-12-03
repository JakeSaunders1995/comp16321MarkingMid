import sys
import os
infolder = sys.argv[1]
outfolder = sys.argv[2]

def morse(cipher):
    old = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '!':'-.-.--', ':':'---...',
                    ';':'-.-.-.', '\'':'.----.','\"':'.-..-.',
                    '-':'-....-','(':'-.--.', ')':'-.--.-'}
    morsecode = {}

    for key, value in old.items():
        morsecode[value] = key

    morsestring = ""

    words = cipher.split("/")
    for word in words:
        letters = word.split()
        newword = ""

        for letter in letters:
            newword += morsecode[letter]

        morsestring += newword + " "

    return morsestring[:-1]

def caeser(cipher):
    cstring = ""
    cipher = cipher.strip()
    cipher = cipher.lower()

    for char in cipher:
        newcharcode = ord(char) - 3
        if newcharcode < 97:
            newcharcode += 26
        newchar = chr(newcharcode)

        if char == " ":
            cstring += char
        else:
            cstring += newchar

    return cstring

def hexadec(cipher):
    cipher = cipher.split()
    hexstring = ""

    for x in cipher:
        newchar = chr(int(x, 16))
        hexstring += newchar

    return hexstring.lower()

for filename in os.listdir(infolder):

    infile = open(infolder + "/" + filename, "r")

    line = infile.readline()
    line = line.split(":")

    if line[0].lower() == "morse code":
        outstring = morse(line[1])
    elif line[0].lower() == "hex" or line[0].lower() == "hexadecimal":
        outstring = hexadec(line[1])
    else:
        outstring = caeser(line[1])

    infile.close()

    outfilename = outfolder + "/" + filename[:-4] + "_h32647nh.txt"
    outfile = open(outfilename, "w")
    outfile.write(outstring)
    outfile.close()
