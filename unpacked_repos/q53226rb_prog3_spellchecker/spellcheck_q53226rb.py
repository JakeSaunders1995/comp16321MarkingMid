import argparse
import os
import string

parser = argparse.ArgumentParser(description = 'Score calculator')
parser.add_argument('Englishwords', help = 'Enter English words list')
parser.add_argument('input', help = 'Enter input path')
parser.add_argument('output', help = 'Enter output path')
args = parser.parse_args()

eng = args.Englishwords
input1 = args.input
output = args.output

file2 = open(eng)
dic1 = file2.read().splitlines()

directory = input1

for filename in (os.scandir(directory)):
	tot2 = 0
	tot = 0
	tot3 = 0
	tot4 = 0
	if filename.is_file():
		file = open(filename)
		text = file.read()

		words = text.split()

	for f in range(len(text)):
		result = ''.join(i for i in text if not i.isdigit())
		new_words = result.split()


	def rep(string):
		punctuation = '''!()-[]{};:'"\,<>./?$%^&*_~''"..."'''
		for e in string:
			if e in punctuation:
				string = string.replace(e, "")
		return string

	new_words3 = []
	new_words2 = [rep(i) for i in new_words]
	for word in range(len(new_words2)):
		new = new_words2[word].lower()
		new_words3.append(new)

	#Sees how many characters are punctuations
	punctuation = '''!()-[]{};:'"\,<>./?$%^&*_~'''''+'...'
	count = 0
	for let in range(len(new_words)):
		for char in range(len(new_words[let])):
			if new_words[let][char] in punctuation:
				count +=1
	tot += count


	counter = 0
	#Sees how many characters are numbers
	for let in range(len(words)):
		for char in range(len(words[let])):
			if words[let][char].isdigit() == True:
				counter +=1
			else:
				continue
	tot2 += counter

	#Sees how many characters are upper case
	count2 = 0
	for let in range(len(words)):
		word = words[let]
		for x in range(len(word)):
			if word[x].isupper() == True:
				count2 +=1
	tot3 += count2

	count3 = 0
	for a in range(len(new_words3)):
		if new_words3[a] !='':
			count3 +=1


	count4 = 0
	for word in range(len(new_words3)):
		for a in range(len(dic1)):
			if new_words3[word].lower() == dic1[a]:
				count4 +=1


	wrong = count3 - count4

	d = os.path.basename(filename)
	x = os.path.splitext(d)[0]
	name = os.path.join(output,str(x)+"_q53226rb.txt")
	file3 = open(name,"a")
	file3.write("q53226rb\nFormatting ###################\nNumber of upper case words changed:"+str(tot3)+"\nNumber of punctuations removed:"+str(tot)+"\nNumber of numbers removed:"+str(tot2)+"\nSpellchecking ###################\nNumber of words:"+str(count3)+"\nNumber of correct words:"+str(count4)+"\nNumber of incorrect words:"+str(wrong))
	file3.close()










