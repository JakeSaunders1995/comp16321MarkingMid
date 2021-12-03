import string
import re
import sys
import os
input_folder = sys.argv[2]
output_folder = sys.argv[3]
input_file = sys.argv[1]
input = os.path.realpath(input_folder)
sum = os.listdir(input)

word = os.path.realpath(input_file)
EnglishWords1 = open(word, "r")
file = EnglishWords1.read()
file = file.split()
EnglishWords1.close()
for me in sum:
    scoring = open(input + "/" + me, 'r')
    message = scoring.read()
    scoring.close()
    output = os.path.realpath(output_folder)
    name = os.path.basename(me)
    name1 = name.replace(".txt", "_q83438yw.txt")
    outcome = open(os.path.join(output, name1), 'w')

    outcome.write("q83438yw")
    outcome.write("\nFormatting ###################")
    r = m = n = q = z = 0
    for i in message:
        if i.isupper():
            r = r + 1
        elif i.isdigit():
            m = m + 1
        elif i.islower():
            n = n + 1
        elif i.isspace():
            z = z + 1
        else:
            q = q + 1
    outcome.write("\nNumber of upper case letters changed: ")
    value1 = str(r)
    outcome.write(value1)
    outcome.write("\nNumber of punctuations removed: ")
    value2 = str(q)
    outcome.write(value2)
    outcome.write("\nNumber of numbers removed: ")
    value3 = str(m)
    outcome.write(value3)
    punctuation_string = string.punctuation
    for i in punctuation_string:
        message = message.replace(i, '')
        message = re.sub('[\d]', '', message)
        message = message.lower()
    outcome.write("\nSpellchecking ###################")
    def word_check(message):
        aa = bb = 0
        for words in message.casefold().split():
            if words in file:
                aa = aa + 1

            else:
                bb = bb + 1
                print(words)

        outcome.write("\nNumber of words: ")
        value4 = str(aa + bb)
        outcome.write(value4)
        outcome.write("\nNumber of correct words : ")
        value5 = str(aa)
        outcome.write(value5)
        outcome.write("\nNumber of incorrect words : ")
        value6 = str(bb)
        outcome.write(value6)
        outcome.close()
    word_check(message)

