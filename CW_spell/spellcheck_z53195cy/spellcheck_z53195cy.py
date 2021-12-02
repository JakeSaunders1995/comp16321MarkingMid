import argparse 
import re

parser = argparse.ArgumentParser(description='encryption')
parser.add_argument('englishWords', type=str, help='english words path')
parser.add_argument('input', type=str, help='output file path')
parser.add_argument('output', type=str, help='output file path')
args = parser.parse_args()

f=open(args.englishWords)
englishwords = f.read()
f.close

f=open(args.input)
text=f.read()
f.close

print('z53195cy')
print('Formatting ###################')


upperword=['A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M']
i = 0 
numberOfUpper = 0
while i < len(text):
	if text[i] in upperword:
		numberOfUpper+=1
		i+=1
	else:
		i+=1
text = text.lower()

# numberOfNumber = 0
# i = 0
# while i < len(text):
# 	if text[i] in range (0,11):
# 		numberOfNumber+=1
# 		i+=1
# 	else:
# 		i+=1
origin = len(text)
text = re.sub(r'[0-9]+', '', text)
numberOfNumber = origin - len(text)

origin=len(text)
text = re.sub('[^\w\s]',"",text)
numberOfPunctuation = origin - len(text) 

print('Number of upper case words transformed: '+str(numberOfUpper))
print('Number of punctuations removed: ' + str(numberOfPunctuation))
print('Number of numbers removed: '+str(numberOfNumber))
print('Spellchecking ###################')
text = re.findall('\w+',text)
englishwords =re.findall('\w+',englishwords)
numberOfWord = len(text)
print('number of words in file: '+str(numberOfWord))

i=0
n = 0
while (i < len(text)):
	if text[i] in set(englishwords):
		n+=1
		i+=1
	else:
		i+=1
			

numberOfcorrect = n
print('Number of correctwords in file: ' + str(numberOfcorrect))
numberofIncorrect = len(text) - numberOfcorrect
print('Number of incorrect words in file: ' + str(numberofIncorrect))

result = ('z53195cy\nFormatting ###################\nNumber of upper case words transforme: '+str(numberOfUpper)+'\nNumber of punctuations removed: '+str(numberOfPunctuation)+'\nNumber of numbers removed: '+str(numberOfNumber)+'\nSpellchecking ###################\nNumber of words in file: '+str(numberOfWord)+'\nNumber of correct words in file: '+str(numberOfcorrect)+'\nNumber of incorrect words in file: '+str(numberofIncorrect))
f = open(args.output,'w')
f.write(result)
f.close