import os, sys

for file in os.listdir(sys.argv[1]):  
    os.chdir('..')
    os.chdir(sys.argv[1])
    ciphertext = open(file, 'r')
    ctext = ciphertext.read()
    text = ctext.rstrip()
    mode = text.split(':')[0]
    unplaintext = text.split(':')[1]
    origintext = ""
    wordtext = ''

    if mode == "Hex":
        code = unplaintext.split(' ')
        unplaintextPosition = 0
        while unplaintextPosition < len(code):
            HexValue = code[unplaintextPosition]
            decimal = int(HexValue, 16)
            char = chr(decimal)
            origintext = origintext + char
            unplaintextPosition += 1

    elif mode == "Caesar Cipher(+3)":
        code = unplaintext.split(' ')
        wordposition = 0
        while wordposition < len(code):
            word = code[wordposition]
            unplaintextPosition = 0
            while unplaintextPosition < len(word):
                char = word[unplaintextPosition]
                charcode = ord(char)
                if 96 < charcode < 100:
                    charcode = charcode + 26
                if char.isalpha():
                    charcode = charcode - 3
                else:
                    charcode = charcode + 0
                wordtext = wordtext + chr(charcode)
                unplaintextPosition += 1
            wordposition += 1
            wordtext = wordtext + ' '
        origintext = origintext + wordtext

    elif mode == "Morse Code":
        codedict = {
            '.-': 'a',
            '-...': 'b',
            '-.-.': 'c',
            '-..': 'd',
            '.': 'e',
            '..-.': 'f',
            '--.': 'g',
            '....': 'h',
            '..': 'i',
            '.---': 'j',
            '-.-': 'k',
            '.-..': 'l',
            '--': 'm',
            '-.': 'n',
            '---': 'o',
            '.--.': 'p',
            '--.-': 'q',
            '.-.': 'r',
            '...': 's',
            '-': 't',
            '..-': 'u',
            '...-': 'v',
            '.--': 'w',
            '-..-': 'x',
            '-.--': 'y',
            '--..': 'z',
            '-----': '0',
            '.----': '1',
            '..---': '2',
            '...--': '3',
            '....-': '4',
            '.....': '5',
            '-....': '6',
            '--...': '7',
            '---..': '8',
            '----.': '9',
        }
        word = ''
        sentence = ''
        code = unplaintext.split('/')
        morseposition = 0

        while morseposition < len(code):
            partword = code[morseposition]
            mochar = partword.split()
            for char in mochar:
                chara = codedict[char]
                word = word + chara
            morseposition += 1
            word = word + ' '
        origintext = word
    os.chdir('..')
    os.chdir(sys.argv[2])
    name = os.path.basename(file).split('.')[0]
    output = open(name+"_y55928xn.txt", 'x')
    output.write(origintext)
