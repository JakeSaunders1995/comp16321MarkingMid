import argparse
import os

puncs = ['.', '?', '!', ',', ':', ';', '-', '_', '(', ')', '[', ']', '{', '}', '~', '"', "'"]
nums = [str(i) for i in range(0, 10)]
upper_char = [chr(i) for i in range(65, 91)]
lower_char = [chr(i) for i in range(97, 123)]
parser = argparse.ArgumentParser()
parser.add_argument('Eword', type=str, help="English word file")
parser.add_argument('inp', type=str, help="path of input file")
parser.add_argument('outp', type=str, help="path of output file")
args = parser.parse_args()
cwords_file = open(args.Eword)
cwords = []
for w in cwords_file:
    cwords.append(w.strip())

if os.path.exists(args.inp):
    files_in = os.listdir(args.inp)
for file in files_in:
    input_file = open(args.inp + '/' + file)
    s = input_file.read()
    input_file.close()
    puc_removed = 0
    num_removed = 0
    upper_trans = 0
    rwords = []
    correct_words = 0
    incorrect_words = 0
    word = ''
    pre_punc = ["", ""]
    for i in s:
        if i in lower_char:
            word += i
            pre_punc=['','']
        elif i in upper_char:
            word += i.lower()
            upper_trans += 1
            pre_punc=['','']
        elif i in puncs:
            puc_removed += 1
            if i == '.' and pre_punc == ['.', '.']:
                puc_removed -= 2
                pre_punc=['','']
            else:
                pre_punc[1] = pre_punc[0]
                pre_punc[0] = i
        elif i in nums:
            num_removed += 1
            pre_punc=['','']
        else:
            pre_punc=['','']
            if word != '': rwords.append(word)
            word = ''
    if word != '': rwords.append(word)
    for w in rwords:
        if w in cwords:
            correct_words += 1
        else:
            incorrect_words += 1

    output_file = open(args.outp + '/' + file[:-4] + "_j23676kd.txt", "w")
    output_file.write("j23676kd")
    output_file.write("\nFormatting ###################")
    output_file.write("\nNumber of upper case letters changed: " + str(upper_trans))
    output_file.write("\nNumber of punctuations removed: " + str(puc_removed))
    output_file.write("\nNumber of numbers removed: " + str(num_removed))
    output_file.write("\nSpellchecking ###################")
    output_file.write("\nNumber of words: " + str(len(rwords)))
    output_file.write("\nNumber of correct words: " + str(correct_words))
    output_file.write("\nNumber of incorrect words: " + str(incorrect_words))
    output_file.close()

