import argparse, os, re
	
parser = argparse.ArgumentParser()
parser.add_argument("words")
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

f_input = os.listdir(args.input)

def spellcheck():

	global sub_text, correct, incorrect, word_count

	if sub_text == "": #just in case the first charcacter is a blank or double blanks

		return

	elif sub_text in word_list: 

		correct += 1

	elif sub_text not in word_list:

		incorrect += 1

	word_count += 1
	sub_text = ""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

with open (args.words) as file:

	word_list = file.read().splitlines()

file.close()

for f in range(len(f_input)):
	
	with open (args.input + "/" + f_input[f], "r") as file:

		raw_text = file.readlines()

	file.close()

	text_list = [" "]
	upper_num = 0
	punct_num = 0
	nums_num = 0
	correct = 0
	incorrect = 0
	word_count = 0

	for i in range(len(raw_text)):

		letters = re.findall("[a-zA-Z ]", raw_text[i])    #Removes punct and nums
		alphanum = re.findall("[a-zA-Z0-9 ]", raw_text[i]) #Removes punct
		upper = re.findall("[A-Z]", raw_text[i])

		text_list.extend(letters)

		punct_num = punct_num + (len(raw_text[i]) - len(alphanum))
		nums_num = nums_num + (len(alphanum) - len(letters))
		upper_num = upper_num + len(upper)

	stripped_text = ""

	for i in range(len(text_list)):

		stripped_text = stripped_text + text_list[i]

	# print(stripped_text)

	sub_text = ""
	stripped_text = stripped_text.lower()

	for i in range(len(stripped_text)): #loops for every character in the stripped out text.

		if stripped_text[i] == " ": #if the character is blank, the current word has ended.

			spellcheck()

		else:

			sub_text = sub_text + stripped_text[i]

	spellcheck()

	f_output = f_input[f][:-4] + "_p23525lg.txt"

	with open (args.output + "/" + f_output, "a") as file:

		file.write("p23525lg\n")
		file.write("Formatting ###################\n")
		file.write("Number of upper case words changed: " + str(upper_num) + "\n") 
		file.write("Number of punctuation removed: " + str(punct_num) + "\n")
		file.write("Number of numbers removed: " + str(nums_num) + "\n")
		file.write("Spellchecking ###################\n")
		file.write("Number of words: " + str(word_count) + "\n")
		file.write("Number of correct words: " + str(correct) + "\n")
		file.write("Number of incorrect words: " + str(incorrect))

	file.close()