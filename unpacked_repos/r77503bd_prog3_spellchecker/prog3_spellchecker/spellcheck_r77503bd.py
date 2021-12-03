import sys 
import re

englishwords = sys.argv[1]
inputfile = sys.argv[2]
outpufile = sys.argv[3]

with open(inputfile, 'r') as fp:
	text= fp.readline()
letters=re.findall('.',text);

with open(englishwords, 'r') as inp:
	dict1 = inp.readlines()
dict2 = []

for z in dict1:
	dict2.append(z.strip("\n"))


punctuationlist = "?/-_()*&^%$£'~#@:;.,<>![]"
punctuation = re.findall('.',punctuationlist)
pandn = "?/-_()*&^%$£'~#@:;.,<>![]1234567890"
check = re.findall('.',pandn)

#def dictionary(englishwords):
	#allwords = []
	#inputfile = open(englishwords, "r")
	#for word in inputfile:

correctstring = ""
cs2 = ""
spellpre = []

UCletters = 0
Punctcount = 0
numbercount = 0


for i in range(0,len(letters)):
	if letters[i] in punctuation:
		Punctcount = Punctcount+1
	#
#for i in range(0,len(letters)):
	elif letters[i].isnumeric():
		numbercount=numbercount+1
		

#for i in range(0,len(letters)):
	elif letters[i].upper() == letters[i] and letters[i] != ' ' and letters[i] not in check and letters[i].isdigit() == False:
		UCletters = UCletters+1
		correctstring += letters[i].lower()

	else:
		
		correctstring += letters[i]


cs1= re.findall('.',correctstring)

for l in cs1:
	if l in check:
		cs1.remove(l)
	
cs2 += correctstring.lower()


cs3 = cs2.split()

for q in cs3:
	if q in check:
		cs3.remove(q)

now = len(cs3)
correct = 0
incorrect = 0 

for word in cs3:
	if word in dict2:
		correct += 1
	else:
		incorrect += 1


#print("{r77503bd}")
#print("Formatting ##################")
#print("Number of upper case letters transformed: " + str(UCletters))
#print("The number of punctuation points removed: " + str(Punctcount))
#print("The number of numbers removed: " + str(numbercount))
#print("Spellchecking ##################")
#print("Number of words: " + str(now))
#print("Number of correct words: " + str(correct))
#print("Number of incorrect words: " + str(incorrect))

output = "r77503bd\n"
output += "Formatting ##################\n"
output += "Number of upper case letters transformed: " + str(UCletters) +"\n"
output += "The number of punctuation points removed: " + str(Punctcount) +"\n"
output += "The number of numbers removed: " + str(numbercount) + "\n"
output += "Spellchecking ##################"+"\n"
output += "Number of words: " + str(now) + "\n"
output += "Number of correct words: " + str(correct) +"\n"
output +="Number of incorrect words: " + str(incorrect) + "\n"

with open(outpufile, 'w') as fp:
	fp.write(output)
