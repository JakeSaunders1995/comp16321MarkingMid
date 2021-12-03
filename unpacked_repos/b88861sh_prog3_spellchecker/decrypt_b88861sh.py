import sys
import codecs
import binascii
import ast

input_filepath = sys.argv[1]
output_filepath = sys.argv[2]


decode = {'.-': 'a',
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
          ' ': ' ',
          '(': '(',
          ')': ')',
          ':': ':',
          '+': '+',
          '\n': '\n',
          '/': ' ',
          '': ''}

encode = {}
for k, v in decode.items():
    encode[v] = k

f = open(input_filepath, 'r', encoding='utf-8')
code = f.read()


if code[0] == 'H':
    f = open(input_filepath, 'r', encoding='utf-8')
    f.seek(4)
    f2 = open(output_filepath, 'w', encoding='utf-8')
    file_contents = f.read()

    words = file_contents.split(' ')

    for word in words:
        f2.write(chr(int(word, 16)))

    f.close()
    f2.close()

elif code[0] == 'C':
    f = open(input_filepath, 'r', encoding='utf-8')
    f.seek(18)
    f2 = open(output_filepath, 'w', encoding='utf-8')
    file_contents = f.read()
    words = str(file_contents)
    all = list(words)
    for j in range(len(all)):
        if all[j] == ' ':
            all[j] = ' '
            continue
        elif all[j] == '\n':
            all[j] = '\n'
            continue
        elif all[j].isupper():
            all[j] = chr((ord(all[j]) - ord('A') - 3) % 26 + ord('A'))
        elif all[j].islower():
            all[j] = chr((ord(all[j]) - ord('a') - 3) % 26 + ord('a'))
    str1 = ''.join(all)
    f2.write(str1)

    f.close()
    f2.close()

elif code[0] == 'M':
    f = open(input_filepath, 'r', encoding='utf-8')
    f.seek(11)
    f2 = open(output_filepath, 'w', encoding='utf-8')
    file_contents = f.read()
    words = file_contents

    all = []
    all = words.split('/ ')
    final = []
    allsp = []
    for i in all:
        allsp = i.split(' ')
        for j in allsp:
            final.append(decode[j])
        final.append(' ')
    strfinal = ''.join(final)
    f2.write(strfinal)
    f.close()
    f2.close()
