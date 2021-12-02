#!/usr/bin/env python

import sys
import os

punctuations = ['.', '?', '!', ',', ':', ';', '-', '—', '(', ')', '[', ']', '{', '}', '<', '>', '’', '\'', '\"', '“', '”', '…']

if(len(sys.argv) != 4):
    print('Incorrect number of arguments. Current number of arguments:' + str(len(sys.argv)))
    exit()

var_capi = 0
var_punc = 0
var_numb = 0

var_word = 0
var_corr = 0
var_inco = 0

def inDict(proposed_word, dict_used):
    global var_word
    global var_corr
    global var_inco
    if(len(proposed_word) != 0):
        var_word = var_word + 1
        if(proposed_word in dict_used):
            var_corr = var_corr + 1
            #print("W(T): " + proposed_word)
        else:
            var_inco = var_inco + 1
            #print("W(F): " + proposed_word)

if(os.path.isdir(sys.argv[2])):
    if not os.path.exists(sys.argv[3]):
        os.makedirs(sys.argv[3])
    with os.scandir(sys.argv[2]) as dirs:
        for entry in dirs:
            current_node = sys.argv[2] + '/' + entry.name 
            node_split = os.path.splitext(current_node)
            filename_with_extension = os.path.basename(current_node)
            filename = filename_with_extension.split('.', 1)[0]
            output_path = sys.argv[3] + '/' + filename + '_j73849yh' + node_split[1]
            if(node_split[1].lower() == '.txt'):
                os.system('python3 ' + sys.argv[0] + ' ' + sys.argv[1] + ' ' + current_node + ' ' + output_path)
    exit()

#print(sys.argv)

fdict = open(sys.argv[1], 'r')
fin = open(sys.argv[2], 'r')

dict_en = fdict.read(-1).split('\n')

tmp_string = str("")
tmp_char = fin.read(1)
dot_count = 0

while(tmp_char!=''):
    if(tmp_char == ' '):
        dot_count = 0
        inDict(tmp_string, dict_en)
        tmp_string = str("")
    elif(tmp_char.isdigit()):
        dot_count = 0
        #print('DIGI: ' + tmp_char)
        var_numb = var_numb + 1
    elif(tmp_char >= 'a' and tmp_char <= 'z'):
        dot_count = 0
        tmp_string = tmp_string + tmp_char
    elif(tmp_char >= 'A' and tmp_char <= 'Z'):
        dot_count = 0
        var_capi = var_capi + 1
        tmp_string = tmp_string + tmp_char.lower()
    elif(tmp_char in punctuations):
        #print('PUNC: ' + tmp_char + str(dot_count))
        var_punc = var_punc + 1
        if(tmp_char == '.'):
            if(dot_count<2):
                dot_count = dot_count + 1
            else:
                #print('PUNC: ...')
                var_punc -= 2
    else:
        dot_count = 0
    tmp_char = fin.read(1)

inDict(tmp_string, dict_en)

fout = open(sys.argv[3], 'w')
fout.write("j73849yh\n")
fout.write("Formatting ###################\n")
fout.write("Number of upper case letters changed: " + str(var_capi) + "\n")
fout.write("Number of punctuations removed: " + str(var_punc) + "\n")
fout.write("Number of numbers removed: " + str(var_numb) + "\n")
fout.write("Spellchecking ###################\n")
fout.write("Number of words: " + str(var_word) + "\n")
fout.write("Number of correct words: " + str(var_corr) + "\n")
fout.write("Number of incorrect words: " + str(var_inco) + "\n")