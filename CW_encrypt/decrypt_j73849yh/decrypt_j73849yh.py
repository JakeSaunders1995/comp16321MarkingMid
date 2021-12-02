#!/usr/bin/env python

import sys
import os

morse = {
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
    '/': ' '
}

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

if(len(sys.argv) != 3):
    print('Incorrect number of arguments.\nCurrent number of arguments:' + str(len(sys.argv)))
    exit()

if(os.path.isdir(sys.argv[1])):
    if not os.path.exists(sys.argv[2]):
        os.makedirs(sys.argv[2])
    with os.scandir(sys.argv[1]) as dirs:
        for entry in dirs:
            current_node = sys.argv[1] + '/' + entry.name 
            node_split = os.path.splitext(current_node)
            filename_with_extension = os.path.basename(current_node)
            filename = filename_with_extension.split('.', 1)[0]
            output_path = sys.argv[2] + '/' + filename + '_j73849yh' + node_split[1]
            if(node_split[1].lower() == '.txt'):
                os.system('python3 ' + sys.argv[0] + ' ' + current_node + ' ' + output_path)
    exit()

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

var_type = fin.read(1)

if(var_type == 'H'):
    fin.read(3)
    var_contents = fin.read(-1)
    characters = var_contents.split(' ')
    for this in characters:
        if(chr(int(this, 16)).lower() in chars):
            fout.write(chr(int(this, 16)).lower())
        
elif(var_type == 'C'):
    fin.read(17)
    var_contents = fin.read(-1)
    for this in var_contents:
        if(this == ' '):
            fout.write(' ')
        elif(this in chars):
            this = ord(this.lower())
            this = this - 3
            if(this < ord('a')):
                this = this + 26
            fout.write(chr(this))

elif(var_type == 'M'):
    fin.read(10)
    var_contents = fin.read(-1)
    characters = var_contents.split(' ')
    for this in characters:
            fout.write(morse[this].lower())