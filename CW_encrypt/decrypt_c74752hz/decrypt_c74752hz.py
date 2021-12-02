import argparse
import os

parse = argparse.ArgumentParser(description='input test file path and output file path')
parse.add_argument('paths', type=str, nargs='+', help='file paths')
args = parse.parse_args()

inputfilelist= []
outputfilelist = []
for outfpath,outdirname,outfilename in os.walk(args.paths[1]):
    continue

for fpath,dirname,fname in os.walk(args.paths[0]):
    for i in fname:
        inputfilelist.append(fpath + '/' + i)
        outputfilelist.append(outfpath + '/' + i[:-4] + '_c74752hz.txt')


def morse(ciphertext):
    morseList = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
        "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
        "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
        "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
        "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")"
}
    string = ''
    list = ciphertext.split(' ')
    for code in list:
        if code == '/':
            string += ' '
        else:
            string += morseList.get(code).lower()
    print(string)
    return string

def hex(ciphertext):
    string = ''
    list = ciphertext.split(' ')
    for i in list:
        dec = int(i,16)
        string += chr(dec).lower()
    print(string)
    return string

def caesar(ciphertext):
    string = ''
    list = ciphertext.split(' ')
    for i in list:
        for j in i:
            char = ord(j.lower())
            if char < 100:
                char +=26
            char -= 3
            string += chr(char)
        string += ' '
    print(string)
    return string

for i in range(len(inputfilelist)):
    with open(inputfilelist[i],mode='r') as f1:
        text = f1.read().strip('\n')
        type,ciphertext = text.split(':')
        # print(type)
        # print(ciphertext)
        if type[0] == 'H' or type[0] == 'h':
            decryptedtext = hex(ciphertext)
        elif type[0] == 'M' or type[0] == 'm':
            decryptedtext = morse(ciphertext)
        elif type[0] == 'C' or type[0] == 'c':
            decryptedtext = caesar(ciphertext)

    with open(outputfilelist[i],mode='w') as f2:
        f2.write(decryptedtext)