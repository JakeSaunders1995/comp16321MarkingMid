import argparse
import os
files = []
sortedfiles = []
b = 0
parser = argparse.ArgumentParser()
parser.add_argument('inputpath')
parser.add_argument('outputpath')
args = parser.parse_args()
inputstream = args.inputpath
outputstream = args.outputpath
print(args.inputpath)
outputfile = ""

for file in os.listdir(inputstream):
    files.append(os.path.join(inputstream, file))

sortedfiles = sorted(files)

MORSE_DICTIONARY = { '.-':'a', '-...':'b',
                    '-.-.':'c', '-..':'d', '.':'e',
                    '..-.':'f', '--.':'g', '....':'h',
                    '..':'i', '.---':'j', '-.-':'k',
                    '.-..':'l', '--':'m', '-.':'n',
                    '---':'o', '.--.':'p', '--.-':'q',
                    '.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w',
                    '-..-':'x', '-.--':'y', '--..':'z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':', ', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-'}

for x in range(len(sortedfiles)):
    working = open(sortedfiles[x], "r")
    whole = working.read()

    ciphertext = whole.split(":")
    plaintext  = ""

    #print(ciphertext[0])
    encryptype = str(ciphertext[0])

    if encryptype[0] == "H" or encryptype[0] == "h":
        print("Type is Hex")
        hexcharacters = ciphertext[1].split()
        for x in range(len(hexcharacters)):
            hex = hexcharacters[x]
            dec = int(hex, 16)
            ascii = chr(int(dec))
            plaintext += ascii

    elif encryptype[0] == "M" or encryptype[0] == "m":
        print("Type is Morse")
        morsewords = ciphertext[1].split(" / ")
        for z in range(len(morsewords)):
            #print(morsewords[z])
            morseletters = morsewords[z].split()
            for a in range(len(morseletters)):
                #print(morseletters[a])
                pattern = morseletters[a]
                plaintext += MORSE_DICTIONARY[pattern]
            plaintext += " "

    elif encryptype[0] == "C" or encryptype[0] == "c":
        print("Type is Caesar")
        caesarcharacters = ciphertext[1].split()
        for x in range(len(caesarcharacters)):
            word = caesarcharacters[x]
            for y in range(len(word)):
                letter = word[y]
                dec = ord(letter)
                if dec == 97:
                    dec = 123
                elif dec == 98:
                    dec = 124
                elif dec == 99:
                    dec = 125
                elif dec == 48:
                    dec = 58
                elif dec == 49:
                    dec = 59
                elif dec == 50:
                    dec = 60
                dec -= 3
                ascii = chr(dec)
                plaintext += ascii
            plaintext += " "

    b += 1
    outputfile = str(outputstream)+'/test_file'+str(b)+'_e11226oc.txt'
    writeout = open(outputfile, "w")
    writeout.write(plaintext)
    print(plaintext)
