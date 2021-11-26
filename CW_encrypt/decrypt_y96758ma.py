import os
import sys
import re

folder=sys.argv[-2]
folderlist = (os.listdir(folder))
folderlist.sort()
folder2=sys.argv[-1]
folderlist2 = os.listdir(folder2)

for folders in folderlist:
    i_file = open(os.path.join(folder, folders))
    readdd = (i_file.read()).strip()
    folderstring=folders.replace(".txt","_y96758ma.txt")
    a=int(0)
    b=int(2)
    test=(readdd[0:3])
    if test == "Hex" or test == "hex":
        a, b=4, 6
        i=0
        count = (len(readdd)-3)/3
        asciii=""
        while i<count:
            code=(readdd[a:b])
            a+=3
            b+=3
            i+=1
            hexx = bytes.fromhex(code)
            ascc = hexx.decode("ASCII")
            asciii+=ascc.lower()
    elif test == "Cae" or test == "cae":
        code=(readdd[18:])
        asciii=""
        for character in code:
            if character.isalpha():
                a = ord(character.lower()) - ord('a')
                character = chr((a - 3) % 26 + ord('a'))
            elif character.isdigit():
                character = str((int(character) - 3) % 10)
            asciii += character
    elif test == "Mor" or test == "mor":
        code=readdd[11:]
        morse =  { 'a':'.-', 'b':'-...',
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
                        '0':'-----', " ":'/'}
        code += ' '
        asciii = ''
        word = ''
        for letter in code:
            if (letter != ' '):
                spaces = 0
                word += letter
            else:
                spaces += 1
                if spaces == 2 :
                    asciii += ' '
                else:
                    asciii += list(morse.keys())[list(morse.values()).index(word)]
                    word = ''

    asciii=str(asciii)
    asciii = re.sub('\s{2,}', ' ', asciii)
    print (asciii.lower())
    o_file = open(os.path.join(folder2, folderstring), 'w')
    o_file.write(asciii)
