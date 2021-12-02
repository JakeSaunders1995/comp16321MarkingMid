import argparse

parser = argparse.ArgumentParser(description="Format the text file and count number of formatted text")
parser.add_argument('file', type=argparse.FileType('r'), help="input a text file with a series of english words")
parser.add_argument('input', type=argparse.FileType('r'), help="input text file")
parser.add_argument('o', type=argparse.FileType('w'), help="output formatted text to a file")
args = parser.parse_args()


# read english file and store it as dictionary to determine the correct words
dictionary = []
idk = args.file.readlines()
for line in idk:
	line = line.rstrip()
	dictionary.append(line)

#read text from input
essay = args.input.read()





upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
u = 0


digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
d = 0


punctuation = ['...','!', '"', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


rmDigit = ''.join(i for i in essay if not i.isdigit())     
#remove digit from the essay
rmPunctuation = "".join(i for i in rmDigit if i not in punctuation)    
#remove punctuation from the essay
changeLower = rmPunctuation.lower()									     
#change to lower case
word_list = changeLower.split()								 
#set all the words into list

print(changeLower)
print(word_list)


i, p = 0, 0
while(i < len(essay)):
	alphabet = essay[i]
	i += 1
	if alphabet in punctuation:
		p += 1
	elif alphabet in upper:
			u += 1
	elif alphabet in digit:
			d += 1
	else:
		continue


start, w, nw = 0, 0, 0
while (start < len(word_list)):
	word = word_list[start]
	start += 1
	if word in dictionary:
		w += 1

	if word not in dictionary:
		nw += 1


print("Number of upper case words transformed:", str(u))
print("Number of punctuation's removed:", str(p))
print("Number of numbers removed:", str(d))
print("Number of words:", str(len(word_list)))
print("Number of correct words in file:", w)
print("Number of incorrect words in file:", nw)

file = args.o.write("m42677js\n")
file = args.o.write("Formatting ###################\n")
file = args.o.write("Number of upper case letters changed: %s \n" % u)
file = args.o.write("Number of punctuations removed: %s \n" % p)
file = args.o.write("Number of numbers removed: %s \n" % d)
file = args.o.write("Spellchecking ###################\n")
file = args.o.write("Number of words: %s \n" % len(word_list))
file = args.o.write("Number of correct words: %s \n" % w)
file = args.o.write("Number of incorrect words: %s \n" % nw)	