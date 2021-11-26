import re
import sys
import string

username = "j33990dk\n"
formatting = "Formatting ###################\n"
spellchecking = "Spellchecking ###################\n"

# read file
file = open(sys.argv[2], "r")
line = file.readline()

# create output file
newFile = open(sys.argv[3], "w")

# remove number
num = sum(i.isdigit() for i in line) #calculate number in text
line1 = ''.join([i for i in line if not i.isdigit()]) # line without number
output_num = "Number of numbers removed: " + f'{num}\n'

# remove punctuation
line2 = line1.replace("...", "") #since ellipsis(...) is considered to be 1 punctuation (more than 1 charater), delete firstly
ellipsis = int((len(line1) - len(line2))/3) # calculate the number of ellipsis in the line
# print(ellipsis)

characters = ['.', '?', '!', ',', ':', ';', '-', '_', '[', ']', '{', '}', '(', ')', '\'', '?',]

line2_list = list(line2) # make list for line1 to compare each character to [characters] to remove

line3_list = [x for x in line2_list if x not in characters]

line3 = "".join(line3_list) # make list2 to str form

punc = (len(line2) - len(line3) + ellipsis) #calculate punctuation in text

output_punc = "Number of punctuations removed: " + f'{punc}\n'

# transform upper to lower
line3 = str(line3)
upper = sum(i.isupper() for i in line3) # calculate upper case
line4 = line3.lower() # transform to lowercase
output_up = "Number of upper case words transformed: " + f'{upper}\n'

# calculate number of words
words = line4.split()
num_words = len(words)
output_num_words = "Number of words in file: " + f'{num_words}\n'

# compare to a list of words
f = open(sys.argv[1], "r")
wordlist = f.read()
wordlist = wordlist.split()

correct = [i for i in words if i in wordlist]
# print(correct)
num_correct = len(correct)
output_num_correct = "Number of correct words in file: " + f'{num_correct}\n'

incorrect = [i for i in words if not i in wordlist]
# print(incorrect)
num_incorrect = num_words - num_correct
output_num_incorrect = "Number of incorrect words in file: " + f'{num_incorrect}\n'

# output file
newFile.write(username)
newFile.write(formatting)
newFile.write(output_up)
newFile.write(output_punc)
newFile.write(output_num)
newFile.write(spellchecking)
newFile.write(output_num_words)
newFile.write(output_num_correct)
newFile.write(output_num_incorrect)

newFile.close()

file.close()