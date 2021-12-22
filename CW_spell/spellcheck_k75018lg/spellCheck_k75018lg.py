import argparse
import os
import re

parser = argparse.ArgumentParser(description='input and output')
parser.add_argument('wordlist', type=str, help='Wordlist')
parser.add_argument('input', type=str, help='Input')
parser.add_argument('output', type=str, help='Output')
args = parser.parse_args()
path1 = args.wordlist
path2 = args.input
path3 = args.output

fl = [i for i in os.listdir(path2)]
filelist1 = [path2 + i for i in os.listdir(path2)]


for files in filelist1:
    index = filelist1.index(files)
    file = open(files)
    read_char = file.read()
    file.close()

    iLetter = 0
    iPunc = -1
    iNumber = 0
    correct_words = 0
    wrong_words = 0
    for i in range(len(read_char)):
        
        if ord(read_char[i]) in range(65, 91):
            iLetter += 1
        
        elif ord(read_char[i]) in range(48, 58):
            iNumber += 1

        elif ord(read_char[i]) in range(97, 123):
            pass

        elif read_char[i] == ' ' or read_char[i] == '   ':
            pass
        
        else:
            iPunc += 1


    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！，0-9]+'
    read_char = re.sub(r, '', read_char)
    read_char = read_char.lower()

 
    read_char = read_char.split()

    
    total_len = len(read_char)

   
    word_list = open(path1, "r")
    lines = word_list.readlines()
    for words in read_char:
        flag = False
       
        for line in lines:
            line = line.rstrip()
            line = line.replace('\n', '').replace('\r', '')
           
            if line == words:
                flag = True
        if flag:
            correct_words += 1

    
    filename = fl[index]
    filename = filename[:-4] + "_k75018lg.txt"
    create = open(path3 + filename, "w")
   
    wrong_words = total_len-correct_words
    create.write("k75018lg\n")
    create.write("Formatting ###################\n")
    create.write("Number of upper case words transformed: %d\n" % iLetter)
    create.write("Number of punctuation’s removed: %d\n" % iPunc)
    create.write("Number of numbers removed: %d\n" % iNumber)
    create.write("Spellchecking ###################\n")
    create.write("Number of words in file: %d\n" % total_len)
    create.write("Number of correct words in file: %d\n" % correct_words)
    create.write("“Number of incorrect words in file: %d\n" % wrong_words)
    create.close()


