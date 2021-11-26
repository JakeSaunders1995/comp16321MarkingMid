import sys 
import os 
import re

dictionary = sys.argv[1]
inputFolder = sys.argv[2]
outputFolder = sys.argv[3]

eng = open(dictionary, "r")
contents = eng.read()
word_check = contents.split("\n")
eng.close()



if os.path.exists(outputFolder) == False:
	os.makedirs(outputFolder)

for input_file in os.listdir(inputFolder):

	file = open(os.path.join(inputFolder, input_file), "r")

	upper_case_letters = 0 
	punctuation = 0
	numbers = 0 
	index = 0 
	ellipsis = 0 


	num_words = 0 
	words_correct = 0 
	words_incorrect = 0
	correct_word = "" 


	for line in file: 

		line = line.split()
		

		for word in line:  

			correct_word = word

			for character in word:


				if character.isnumeric() == True:
					correct_word = re.sub(character, "", correct_word, 1)
					numbers = numbers + 1 

				elif character in ".?!,:;-— –'`[]\{}()":

					if character == ".":
						index = word.index(character)

						try:

							if ellipsis > 0:
								ellipsis = ellipsis - 1 

							elif word[index + 1] == character and word[index + 2] == character:
								punctuation = punctuation + 1 
								ellipsis = 2 
								correct_word = re.sub("\.", "", correct_word, 3)


						except:
							punctuation = punctuation + 1 
							correct_word = re.sub("\.", "", correct_word, 1)
							ellipsis = 0 

					elif character in "[{()":
						punctuation = punctuation + 1
						correct_word = re.sub("\\" + character, "", correct_word, 1)

					else: 

						punctuation = punctuation + 1 

						correct_word = re.sub(character, "", correct_word, 1)

				elif character.isupper() == True: 
					correct_word = re.sub(character, character.lower(), correct_word, 1)
					upper_case_letters = upper_case_letters + 1 

			# check to see if string is not an empty string 

			if correct_word != "":

				num_words = num_words + 1

				if correct_word in word_check:
					words_correct = words_correct + 1 

				else: 
					words_incorrect = words_incorrect + 1 



	file.close()

	name, ext = os.path.splitext(input_file)
	output_file = name + "_h64411rs" + ext 

	file = open(os.path.join(outputFolder, output_file), "w")
	file.write("h64411rs \n")
	file.write("Formatting ################## \n")
	file.write("Number of upper case letters changed: " + str(upper_case_letters) + "\n")
	file.write("Number of punctuations removed: " + str(punctuation) + "\n")
	file.write("Number of numbers removed: " + str(numbers) + "\n")
	file.write("Spellchecking ################# \n")
	file.write("Number of words: " + str(num_words) + "\n")
	file.write("Number of correct words: " + str(words_correct) + "\n")
	file.write("Number of incorrect words: " + str(words_incorrect))
	file.close()












