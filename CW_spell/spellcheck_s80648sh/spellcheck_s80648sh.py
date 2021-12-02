import os
import sys
import string

def do_spellcheck(input_file,output_file,english_words):
	
	def get_text():
		file = open(input_file)
		text = file.read()
		file.close()
		return text

	def format_text(text):

		def lowercase(text):
			no_upper_text = text.lower()
			count = 0
			for i in range (0, len(no_upper_text)-1):
				if text[i] != no_upper_text[i]:
					count +=1
			
			file = open(output_path,"a")
			file.write(f"Number of upper case words changed: {count}\n")
			file.close()
			return no_upper_text

		def no_punctuation(text):
			no_punc = ""
			punctuation = ""
			punctuation = punctuation + '"' 
			punctuation = punctuation + "!'(),-./:;?[]_`{|}~…"

			count = 0
			for i in range(0,len(text)):
				has_punc = False
				for z in range (0,len(punctuation)):
					if text[i] == punctuation[z]: 
						has_punc = True
						count +=1
				if has_punc == False:
					no_punc = no_punc+ text[i]

			file = open(output_path,"a")
			file.write(f"Number of punctuations removed: {count}\n")
			file.close()

			return no_punc

		def no_numbers(text):
			count = 0

			for character in text:
				if character.isdigit():
					count +=1
					text = text.replace(character,"")
			file = open(output_path,"a")
			file.write(f"Number of numbers removed: {count}\n")
			file.close()
			return text


		no_upper_text = lowercase(text)
		no_punctuation_text = no_punctuation(no_upper_text)
		no_numbers_text = no_numbers(no_punctuation_text)
		formatted_text = no_numbers_text.replace("  "," ")

		return formatted_text

	def spell_check(text):
		word_file = open(english_words)
		all_words = word_file.readlines()
		word_list = []
		for line in all_words:
			word_list.append(line.rstrip())

		word_file.close
		number_correct = 0

		text_words = text.split(" ")
		
		for word in text_words:
			for word2 in word_list:
				if word == word2:
					number_correct+=1



		return number_correct


	text = get_text()

	# output_path = input_file.replace(".txt","")
	# output_path = output_path.replace("./Example_inputs_program3","")
	# output_path = output_path + "_s80648sh.txt"
	# output_path = (output_folder + output_path).replace("//","/")

	input_file = input_file.replace(".txt","_s80648sh.txt")
	position_change = input_file.index("//")
	new_file = input_file[position_change +1:]
	print(new_file)
	output_path = output_folder + new_file	
	output_path = output_path.replace("//","/")

	file = open(output_path,"a")

	file.write("s80648sh\n")
	file.write("Formatting ###################\n")
	file.close()

	formatted_text = format_text(text)

	words = formatted_text.split(" ")
	num_words = len(words)
	num_correct = spell_check(formatted_text)
	num_incorrect = num_words - num_correct

	file = open(output_path,"a")
	file.write("Spellchecking ###################\n")
	file.write(f"Number of words: {num_words}\n")


	file.write(f"Number of correct words: {num_correct}\n")
	file.write(f"Number of incorrect words: {num_incorrect}\n")
	file.close()

english_words = sys.argv[1]

input_folder = sys.argv[2]
if input_folder[-1] != "/":
	input_folder = input_folder + "/"
if input_folder[0] != "/":
	input_folder = "/" + input_folder

output_folder= sys.argv[3]
if output_folder[-1] != "/":
	output_folder = output_folder + "/"
	print(output_folder)
if output_folder[0] != "/":
	output_folder = "/" + output_folder
	print(output_folder)

input_files = os.listdir(input_folder)
input_files.sort()

print(input_files)

for i in range(0,len(input_files)):
	do_spellcheck(input_folder + "/" + input_files[i],output_folder,english_words)
