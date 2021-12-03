import argparse, string, os
# parser = argparse.ArgumentParser(description = "decryption of 3 types")
# parser.add_argument('input', help='the input directory')
# parser.add_argument('input2', type = argparse.FileType('r'))
# parser.add_argument('output', help='the output directory')
# args = parser.parse_args()


# path = args.input
# English_words = args.input2
# path_output = args.output

def spellcheck(file):
	# check = English_words.read()
	Text = file
	words = Text.split()
	checked_splitted = check.split()
	punctuation = ['!','"','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','[',']','^','_','`','{','|','}','~','...','–']
	punctuation_removed = 0
	numbers_removed =0
	upper_transformed = 0
	correct_words = []
	incorrect_words =[]
	# number_words = len(words)


	def split(Text): 
		charechters = [letter for letter in Text.strip()]
		for p in range(len(charechters)-2):
			if charechters[p:p+3] == ['.','.','.']:
				charechters[p:p+3] = ['...']

		return charechters

	
	
	corrected_sentence =""
	for i in split(Text):
		if i in punctuation:
			punctuation_removed +=1
			i=""
			corrected_sentence+=i
		if i.isdigit() == True:
			numbers_removed +=1
			i=""
			corrected_sentence+=i
		if i.isupper():
			upper_transformed +=1
			i = i.lower()
			corrected_sentence+=i
		else:
			corrected_sentence+=i

	correct = corrected_sentence.split()
	for w in correct:
		if w in checked_splitted:
			correct_words.append(w)
		else:
			incorrect_words.append(w)

	number_correct = len(correct_words)
	number_incorrect = len(incorrect_words)
	number_words = len(correct)

		#for engwords in range(len(checked_splitted)):
		#	if words[w] == checked_splitted[engwords] :
		#		correct_words += words[w]
		#	else:
		#		incorrect_words += words[w]
	#new_list = str.maketrans("","",string.punctuation)
	#strip =[i.translate(new_list) for i in words]
	#print(new_list)

	print(corrected_sentence)
	answers = f'username [m46198sa] \n Formatting ################### \n Number of upper case words transformed:{upper_transformed} \n Number of punctuation’s removed:{punctuation_removed} \n Number of numbers removed:{numbers_removed} \n Spellchecking ################### \n Number of words in file:{number_words} \n Number of correct words in file:{number_correct} \n Number of incorrect words in file:{number_incorrect}'
	print(answers)
	return answers


parser = argparse.ArgumentParser(description = "decryption of 3 types")
parser.add_argument('input2', type = argparse.FileType('r'))
parser.add_argument('input', help='the input directory')
parser.add_argument('output', help='the output directory')
args = parser.parse_args()


English_words = args.input2
path = args.input
path_output = args.output
check = English_words.read()

for file in os.listdir(path):
	with open(path+"/"+file, 'r') as f:
		with open(path_output + "/" + file.replace(".txt","_m46198.txt"),"w") as n:
			n.write(spellcheck(f.read()))

