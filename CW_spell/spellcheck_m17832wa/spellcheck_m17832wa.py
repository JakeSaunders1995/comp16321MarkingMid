import sys, os, re

username = "m17832wa"
words_file = sys.argv[1]
input_folder = sys.argv[2]
output_folder = sys.argv[3]

if input_folder[-1] != "/":
	input_folder += "/"
if output_folder[-1] != "/":
	output_folder += "/"

input_files = os.listdir(input_folder)

for file in range(len(input_files)):
	input_file = open(input_folder + input_files[file], "r")
	input_file_words = input_file.read()
	input_file_words = re.split(' |\n', input_file_words)

	if input_files[file] == "test_file4.txt":
		print(input_file_words)
		print(len(input_file_words))

	uppers = punctuation = numbers_count = 0

	def clean(word_list):
		global uppers, punctuation, numbers_count

		word = 0
		while word < len(word_list):
			char = 0
			toRemove = []
			while char < len(word_list[word]):
				if word_list[word][char] == word_list[word][char].upper() and word_list[word][char].isalpha() == True:
					uppers += 1
					char += 1
				elif word_list[word][char].isnumeric() == True:
					numbers_count += 1
					toRemove.append(word_list[word][char])
					char += 1
				elif word_list[word][char].isnumeric() == False and word_list[word][char].isalpha() == False and word_list[word][char] != "#" and word_list[word][char] != "@":
					# elipses checking
					if word_list[word][char] == ".":
						print(". found", word_list[word], word_list[word][char])
						try:
							if word_list[word][char + 1] == "." and word_list[word][char + 2] == ".":
								punctuation += 1
								toRemove.append(word_list[word][char])
								toRemove.append(word_list[word][char + 1])
								toRemove.append(word_list[word][char + 2])
								char += 3
						except:
							punctuation += 1
							toRemove.append(word_list[word][char])
							char += 1
					else:
						punctuation += 1
						toRemove.append(word_list[word][char])
						char += 1
				else:
					char += 1

			for character in toRemove:
				word_list[word] = word_list[word].replace(str(character), '')

			word_list[word] = word_list[word].lower()

			word += 1

		words = 0
		while words < len(word_list):
			if word_list[words] == "":
				word_list.pop(words)
			else:
				words += 1

		return word_list

	cleaned_words = clean(input_file_words)

	def spellCheck(word_list):
		words_file_opened = open(words_file, 'r')
		words = words_file_opened.readlines()

		for i in range(len(words)):
			words[i] = words[i].strip('\n')

		correct_words = 0
		incorrect_words = 0

		for word in word_list:
			if word in words:
				correct_words += 1
			else:
				incorrect_words += 1
				print(word)

		return correct_words, incorrect_words

	cleaned_words = clean(input_file_words)
	correct_words, incorrect_words = spellCheck(cleaned_words)

	fileName = str(input_files[file]).replace('.txt', '')
	output_file_loc = output_folder + fileName + "_m17832wa.txt"

	with open(output_file_loc, "w") as output_file:
		output = username + "\n"
		output += "Formatting ###################\n"
		output += "Number of upper case letters changed: " + str(uppers) + "\n"
		output += "Number of punctuations removed: " + str(punctuation) + "\n"
		output += "Number of numbers removed: " + str(numbers_count) + "\n"
		output += "Spellchecking ###################\n" 
		output += "Number of words: " + str(len(input_file_words)) + "\n"
		output += "Number of correct words: " + str(correct_words) + "\n"
		output += "Number of incorrect words: " + str(incorrect_words) + "\n"

		output_file.write(output)