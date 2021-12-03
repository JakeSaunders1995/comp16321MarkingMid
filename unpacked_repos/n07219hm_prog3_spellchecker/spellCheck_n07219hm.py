#spellcheck
from sys import argv
from os import listdir
print("If a FileNotFoundError occurs please use a '/' at the end of the input and output folder paths")
global dict_file_path
dict_file_path = argv[1]
global input_folder_path
input_folder_path = argv[2]
global output_folder_path
output_folder_path = argv[3]
global username
username = "n07219hm"





#write results to text file
def write_output(path,nums,puncs,total,correct,incorrect,uppers):
	output_file = open(path,"w")
	output_file.write(str(username) + "\n" + "Formatting ###############\n" + "Number of upper case words changed: " + str(uppers) + "\n" + "Number of punctuations removed: " + str(puncs) + "\n" + "Number of numbers removed: " + str(nums) + "\n" + "SpellChecking ###############\n" + "Number of words: " + str(total) + "\n" + "Number of correct words: " + str(correct) + "\n" + "Number of incorrect words: " + str(incorrect) + "\n")
	output_file.close()

# Read and format the input text for processing while keeping track of what has been done e.g number of punctuations removed. Returns lis of individual words
def format_input_file(path):
	
	input_file = open(path,"r")
	lines_list_with_upper = input_file.readlines()
	input_file.close()
	

	#remove capitals
	global uppercases_removed
	uppercases_removed = 0
	lines_list = []
	for line in lines_list_with_upper:
		for char in line:
			if char.isupper():
				line = line.replace(char,char.lower())
				uppercases_removed += 1
		lines_list.append(line)


	
	
	#remove blank lines
	
	lines_to_delete = []
	for i in range(0,len(lines_list)):
		if lines_list[i] == "":
		 	lines_to_delete.append(lines_list[i])
	for line in lines_to_delete:
		lines_list.remove(line)

	#remove punctuation and numbers
	global punctuation_removed
	punctuation_removed = 0
	global numbers_removed
	numbers_removed = 0

	processed_lines_list = []
	punctuation = [".", "?", "!", ",", ":", ";", "-", "(", ")", "{", "}", "[", "]","'", '"']
	numbers = ["0","1","2","3","4","5","6","7","8","9"]
	#list_for_elip_check = []
	period_count = 0
	for line in lines_list:
		for char in line:
			if char == ".":
				period_count += 1
			else:
				period_count = 0
			if char in punctuation:
				#list_for_elip_check.append(char)
				line = line.replace(char,"")
				punctuation_removed += 1
				
			if char in numbers:
				line = line.replace(char,"")
				numbers_removed += 1
			if period_count == 3:
				punctuation_removed -=2
		processed_lines_list.append(line)

	#elipsis check
	# for i in range(0,len(list_for_elip_check)-2):
	# 	if list_for_elip_check[i] == "." and list_for_elip_check[i+1] == "." and list_for_elip_check[i+2] == ".":
	# 		punctuation_removed -= 2

	#split lines into words
	temp_word_list = []
	for line in processed_lines_list:
		temp_word_list.append(line.split(" "))
	#turn into one big list instead of a 2d array
	word_list = []
	for sublist in temp_word_list:
		for word in sublist:
			word_list.append(word)
	#remove blank entries and new lines as removing punctuationcan create them
	count_blank = 0
	count_newline = 0
	for word in word_list:
		if word == "":
			count_blank +=1
		if word == "\n":
			count_newline += 1
	for i in range(0,count_newline):
		word_list.remove("\n")
	for i in range(0,count_blank):
		word_list.remove("")
	print(word_list)
	return word_list




# Function will compare words to the dictionary and tally how many correct and incorrect words there are 
def checkSpelling(dictionary,words):
	dict_file = open(dictionary,"r")
	dict_file_content = dict_file.readlines()
	dict_file.close
	global correct_words
	correct_words = 0
	global incorrect_words
	incorrect_words = 0

	for word in words:
		
		if word + "\n" in dict_file_content:
			correct_words += 1
		else:
			incorrect_words += 1
			print(word)

	global total_words
	total_words = incorrect_words + correct_words
	#call file output function
	
	

#Looping through files
file_list = listdir(input_folder_path)
output_file_list = []
for file in file_list:
	output_file_list.append(file[:-4] + "_" + username + ".txt")

for i in range(0,len(file_list)):
	output_file_path = output_folder_path + output_file_list[i] 
	checkSpelling(dict_file_path, format_input_file(str(input_folder_path) + file_list[i]))
	write_output(output_file_path, numbers_removed, punctuation_removed, total_words, correct_words, incorrect_words, uppercases_removed)



