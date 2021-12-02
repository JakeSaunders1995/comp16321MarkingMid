import os, sys


def check(string: str):
	string_formatted = ""
	num_uppercase = 0
	num_punctuation = 0
	num_numbers = 0
	num_words = 0
	num_correct = 0
	num_incorrect = 0
	accum_period = 0

	for char in string:
		if char != char.lower():
			num_uppercase += 1
			string_formatted += char.lower()
		elif char in ".?!,:;—-()[]{}'\"…":
			num_punctuation += 1
		elif char in "0123456789":
			num_numbers += 1
		elif char.lower() in "abcdefghijklmnopqrstuvwxyz ":
			string_formatted += char.lower()

		if char == ".":
			accum_period += 1
			if accum_period == 3:
				num_punctuation -= 2
				accum_period = 0
		else:
			accum_period = 0

	word_list = string_formatted.split()
	num_words = len(word_list)
	for word in word_list:
		if word in english_words:
			num_correct += 1
		else:
			num_incorrect += 1

	output = "n96249ty\n"
	output += "Formatting ###################\n"
	output += f"Number of upper case letters changed: {num_uppercase}\n"
	output += f"Number of punctuations removed: {num_punctuation}\n"
	output += f"Number of numbers removed: {num_numbers}\n"
	output += "Spellchecking ###################\n"
	output += f"Number of words: {num_words}\n"
	output += f"Number of correct words: {num_correct}\n"
	output += f"Number of incorrect words: {num_incorrect}"
	return output


file = open(sys.argv[1])
english_words = [english_word.rstrip("\n") for english_word in file.readlines()]
file.close()

for filename in os.listdir(sys.argv[2]):
	if filename.endswith(".txt"):
		file = open(f"{sys.argv[2]}/{filename}")
		string = file.readlines()
		string = [s.rstrip("\n") for s in string]
		string = " ".join(string)
		file.close()

		output = check(string)
		print(filename)
		filename = filename[:-4]
		file = open(f"{sys.argv[3]}/{filename}_n96249ty.txt", "w")
		file.write(output)
		file.close()
