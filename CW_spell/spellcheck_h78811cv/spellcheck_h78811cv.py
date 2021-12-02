import sys, os
 
def open_file(file):
		filename = open(file, "r")
		content = filename.read()
		filename.close()
		return content

punctuation = "!():;{[]'},./?-—"+'"'
numbers = "0123456789"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_directory = sys.argv[2]
file_list = os.listdir(input_directory)

x = 0
while x <= len(file_list)-1:

	upper_transformed = 0
	punctuation_removed = 0
	numbers_removed = 0
	word_count = 0
	correct_words = 0
	incorrect_words = 0

	english_file = open_file(sys.argv[1])
	input_file = open_file(input_directory+"/"+file_list[x])

	j = input_file.count("...")
	input_file = input_file.replace("...", "")
	punctuation_removed += j

	i = 0
	for character in input_file:
		if character in upper:
			upper_transformed += 1
			input_file = input_file.replace(input_file[input_file.index(character)], character.lower(), 1)
		if character in punctuation:
			punctuation_removed += 1
			input_file = input_file.replace(input_file[input_file.index(character)], "", 1)
		if character in numbers:
			numbers_removed += 1
			input_file = input_file.replace(input_file[input_file.index(character)], "", 1)
		
	new_contents = input_file.split()
	english_list = english_file.split()

	for word in new_contents:
		if word in english_list:
			correct_words += 1
		else:
			incorrect_words += 1

	filename = str(file_list[x]).replace(".txt", "")
	ouput_directory = sys.argv[3]
	output_file = open(ouput_directory+"/"+filename+"_h78811cv.txt", "w")
	output_file.write("h78811cv\n")
	output_file.write("Formatting ###################\n")
	output_file.write("Number of upper case words changed: "+str(upper_transformed)+"\n")
	output_file.write("Number of punctuation’s removed: " + str(punctuation_removed)+"\n")
	output_file.write("Number of numbers removed: " + str(numbers_removed)+"\n")
	output_file.write("Spellchecking ###################\n")
	output_file.write("Number of words in file: " + str(len(new_contents))+"\n")
	output_file.write("Number of correct words in file: " + str(correct_words)+"\n")
	output_file.write("Number of incorrect words in file: " +str(incorrect_words)+"\n")
	output_file.close()
	x+=1