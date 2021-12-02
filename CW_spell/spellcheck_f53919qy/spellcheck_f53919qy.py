import re
import sys

COUNT_UPPER = 0
COUNT_PUNCTUATION = 0
COUNT_NUMBER = 0
COUNT_WORD = 0
COUNT_CURRECT_WORD = 0
COUNT_INCORRECT_WORD = 0


english_words_path = sys.argv[1]
input_file_path = sys.argv[2]
output_file_path = sys.argv[3]

dict = []
with open(english_words_path, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        dict.append(line)


with open(input_file_path, 'r') as f:
    context = f.read()

for c in context:
    if c.isupper():
        COUNT_UPPER += 1
    elif c.isdigit():
        COUNT_NUMBER += 1
    else:
        COUNT_PUNCTUATION += 1

context = context.lower()

remove_chars = '[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
context = re.sub(remove_chars, '', context)

word_list = context.split()

COUNT_WORD = len(word_list)

for word in word_list:
    if word in dict:
        COUNT_CURRECT_WORD += 1

COUNT_INCORRECT_WORD = COUNT_WORD - COUNT_CURRECT_WORD

output = ""
output += "f53919qy" + "\n"
output += "Formatting ###################" + "\n"
output += "Number of upper case words changed: " + str(COUNT_UPPER) + "\n"
output += "Number of punctuations removed: " + str(COUNT_PUNCTUATION) + "\n"
output += "Number of numbers removed: " + str(COUNT_NUMBER) + "\n"
output += "Spellchecking ###################" + "\n"
output += "Number of words in file: " + str(COUNT_WORD) + "\n"
output += "Number of correct words in file: " + str(COUNT_CURRECT_WORD) + "\n"
output += "Number of incorrect words in file: " + str(COUNT_INCORRECT_WORD) + "\n"

with open(output_file_path, 'w') as f:
    f.write(output)