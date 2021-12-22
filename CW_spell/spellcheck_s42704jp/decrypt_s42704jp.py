import sys
import codecs
import binascii
import ast

input_filepath = sys.argv[1]
output_filepath = sys.argv[2]


print("input File path : " + input_filepath)
print("ouput File path : " + output_filepath)

dec_dic = {'.-': 'a',
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
           '.----': '1',
           '..---': '2',
           '...--': '3',
           '....-': '4',
           '.....': '5',
           '-....': '6',
           '--...': '7',
           '---..': '8',
           '----.': '9',
           '-----': '0',
           ' ': ' ',
           '(': '(',
           ')': ')',
           ':': ':',
           '+': '+',
           '\n': '\n',
           '/': ' ',
           '': ''
           }

enc_dic = {}
for k, v in dec_dic.items():
    enc_dic[v] = k

f = open(input_filepath, 'r', encoding='utf-8')
how = f.read()
f.seek(0)
f.close()

if 'Morse Code' in how:
    f = open(input_filepath, 'r', encoding='utf-8')
    f.seek(11)
    f2 = open(output_filepath, 'w', encoding='utf-8')
    file_contents = f.read()
    words = file_contents

    allstr = []
    allstr = words.split('/ ')
    allstr2 = []
    str1 = []
    for i in allstr:
        str1 = i.split(' ')
        for j in str1:
            print(j)
            allstr2.append(dec_dic[j])
        allstr2.append(' ')
    str123 = ''.join(allstr2)
    f2.write(str123)
    f.close()
    f2.close()


elif 'Caesar' in how:
    f = open(input_filepath, 'r', encoding='utf-8')
    f.seek(18)
    f2 = open(output_filepath, 'w', encoding='utf-8')
    file_contents = f.read()
    words = str(file_contents)
    allstr = list(words)
    for j in range(len(allstr)):
        if allstr[j] == ' ':
            allstr[j] = ' '
            continue
        if allstr[j] == '\n':
            allstr[j] = '\n'
            continue
        if allstr[j].isupper():
            allstr[j] = chr((ord(allstr[j]) - ord('A') - 3) % 26 + ord('A'))
        elif allstr[j].islower():
            allstr[j] = chr((ord(allstr[j]) - ord('a') - 3) % 26 + ord('a'))
    str1 = ''.join(allstr)
    f2.write(str1)

    f.close()
    f2.close()
 

if 'Hex' in how:
    f = open(input_filepath, 'r', encoding='utf-8')
    f.seek(4)
    f2 = open(output_filepath, 'w', encoding='utf-8')
    
    file_contents = f.read()

    words = file_contents.split(' ')

    for word in words:
        f2.write(chr(int(word, 16)))

    f.close()
    f2.close()
    
