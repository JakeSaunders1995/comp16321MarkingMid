import sys
import re
import string


english_filepath = sys.argv[1]
input_filepath = sys.argv[2]
output_filepath = sys.argv[3]


f = open(input_filepath, 'r', encoding='utf-8')
f2 = open(output_filepath, 'w', encoding='utf-8')
f3 = open(english_filepath, 'r', encoding='utf-8')

text = f.read()

Upper = 0
Punct = 0
Remove = 0
total = 0
correct = 0
incorrect = 0
allstr = []
allstr2 = []

wd = f3.read()
wordlist = []
wordlist = wd.split("\n")

for i in range(len(text)):
    if (text[i] == "." or text[i] == '?' or text[i] == '!' or text[i] == "," or text[i] == ':' or text[i] == ';' or
            text[i] == '—' or text[i] == '-' or text[i] == '[' or text[i] == ']' or text[i] == '{' or text[i] == '}' 
            or text[i] == '(' or text[i] == ')' or text[i] == "'" or text[i] == '"' or text[i] == '...'):
        Punct = Punct + 1
        allstr2.append('')
        continue
    elif (text[i] == '1' or text[i] == '2' or text[i] == '3' or text[i] == '4' or text[i] == '8' or text[i] == '7' or
          text[i] == '6' or text[i] == '5' or text[i] == '9' or text[i] == '0'):
        Remove = Remove + 1
        allstr2.append('')
        continue
    elif (text[i].isupper()):
        Upper = Upper + 1
        allstr2.append(text[i].lower())
        continue
    else:
        allstr2.append(text[i])


#remove number
line1 = text
line2 = re.sub("[0-9]","",line1)

#remove punctuation
line3 = line2.translate(str.maketrans('','',string.punctuation))

#transform upper into lower
line4 = line3.lower()


line4_str = ''.join(line4)
newline = []
newline = line4_str.split(" ")
perfect = []
for i in range(len(newline)):
    check = newline[i].strip()
    if ' ' not in check and check != '':
        total += 1
        perfect.append(check)
total = len(perfect)

for i in range(len(perfect)):
    if perfect[i] not in wordlist:
        incorrect += 1
        i += 1
correct = total - incorrect


f2.write('b88861sh\n')
f2.write("Formatting ###################\n")
f2.write(f'Number of upper case words changed: {Upper}\n')
f2.write(f'Number of punctuations removed: {Punct}\n')
f2.write(f'Number of numbers removed: {Remove}\n')
f2.write(f'Spellchecking ###################"\n')
f2.write(f'Number of words: {total}\n')
f2.write(f'Number of correct words: {correct}\n')
f2.write(f'Number of incorrect words: {incorrect}\n')
