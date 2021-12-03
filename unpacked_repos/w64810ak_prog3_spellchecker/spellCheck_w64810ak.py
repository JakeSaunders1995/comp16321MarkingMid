import re
import argparse
import os

parser = argparse.ArgumentParser(description='Add file path')
parser.add_argument('englishWords', type=str, help="englishtxt")
parser.add_argument('input', type=str, help="file path")
parser.add_argument('output', type=str, help='filepath')

args = parser.parse_args()

def spellCheck(filepath):

    f = open(filepath)
    substring = (f.read())
    # print(substring)
    numbers = 0

    substring.count("")


    f = open(args.englishWords)
    english_words = (f.read())
    english_words_list = english_words.split()

    result = ''.join([i for i in substring if not i.isdigit()])


    punctuation = '.,/!?:;'
    punct_pointer=0
    for i in result:
        if i in punctuation:
            punct_pointer +=1
            result = result.replace(i, "")

    # print(result.lower())
    # print(result[3])
    word_list = result.split()

    word_count = 0
    for i in word_list:
        word_count += 1

    correct_words = []
    incorrect_words = 0
    for i in range (len(word_list)):
        if word_list[i] in english_words_list:
            correct_words.append(word_list[i])
            # print(correct_words)

        else:
            incorrect_words +=1
            # print(incorrect_words)
    count = 0
    for i in correct_words:
        count += 1

    ("Number of numbers removed: ", )
    f = open(args.output+filename, "a")
    f.write("Spellchecking########### \n")
    f.write("Number of words in file: " + str(word_count)+'\n'+"Number of correct words in file: " + str(count)+'\n'+"Number of incorrect words in file: " + str(word_count - count)
    +'\n'+"Number of incorrect words in file: " + str(word_count - count)+'\n'+"Number of punctuation's removed: " + str(punct_pointer))
    f.close()
    file_change = (os.path.splitext(args.output+filename)[0])
    # print(file_change)
    # os.rename(file_change, file_change + '_w64810ak.txt')
    old_file = os.path.join(args.output, filename)
    new_file = os.path.join(args.output, file_change+'_w64810ak.txt')
    os.rename(old_file, new_file)





if __name__ == '__main__':
    for filename in os.listdir(args.input):
        if filename.endswith(".txt"):
            spellCheck(args.input+ '/' +filename)
