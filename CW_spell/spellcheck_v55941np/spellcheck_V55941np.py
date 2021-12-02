import sys
import os

def spellcheck(filename):
	input_file = input_folder + "/" + filename 
	input_file = open(input_file,"r")
	output_file = filename[:-4]
	output_file = output_file+"_V55941np.txt"
	new_output_file = output_folder + "/" + output_file
	output_file = open(new_output_file,"w+")
	old_data = input_file.readlines()
	for i in range(0,len(old_data)):
		old_data[i] = old_data[i].strip("\n")
	number_count = 0
	punctuation_count = 0
	uppercase_letters= 0
	correct_words = 0 
	incorrect_words = 0
	word_count = 0
	for data in old_data:
		x = 0
		while x < len(data): #checks for punctuation and numbers
			ellipsis = False
			if data[x] not in alphabet:
				if data[x] in numbers:
					number_count += 1
				elif data[x] == " ":
					pass
				else:
					if data[x] != "#" or data[x] != "@":
						punctuation_count += 1
					if data[x] == ".":
						if x < len(data)-2:
							if data[x+1] == "." and data[x+2] == ".":
								x +=3
								ellipsis = True
			if ellipsis == False:
				x+= 1

		data_words = []	
		word = ""
		for i in data: #removes all numbers and punctuation and also spaces
			if i in alphabet or i == "'":
				if i == "'":
					pass
				else:
					word = word + i
			else:
				if len(word) >0:
					data_words.append(word)
					word = ""
		if len(word)>0 and word != data_words[len(data_words)-1]:
			data_words.append(word)

		new_data_words = [] #checks for any words that have uppercases in them and then changes them
		for i in data_words:
			if i.lower() != i:
				for j in i:
					if j.lower() != j:
						uppercase_letters += 1
			new_data_words.append(i.lower())

		
		for i in new_data_words: #checks for correct words
			if i in english_words:
				correct_words += 1
				word_count+=1
			else:
				incorrect_words += 1
				word_count+=1

	output_file.write("V55941np\n") #writes to the file in the correct format
	output_file.write("Formatting ###################\n")
	output_file.write("Number of upper case letters changed: "+str(uppercase_letters)+"\n")
	output_file.write("Number of punctuations removed: "+str(punctuation_count)+"\n")
	output_file.write("Number of numbers removed: "+str(number_count)+"\n")
	output_file.write("Spellchecking ###################\n")
	output_file.write("Number of words: "+str(word_count)+"\n")
	output_file.write("Number of correct words: "+str(correct_words)+"\n")
	output_file.write("Number of incorrect words: "+str(incorrect_words)+"\n")
	
words = open(sys.argv[1],"r")
english_words = []
for line in words:
	english_words.append(line.strip("\n")) #creates an array of words from txt file


input_folder = sys.argv[2]
output_folder = sys.argv[3]
try: #creates a folder if there isn't one
	os.mkdir(output_folder)
except OSError as error:
	pass

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

arr = os.listdir(input_folder)
for i in range(0,len(arr)):
	spellcheck(arr[i])

#command i used to test ignore
#python3 spellCheck_V55941np.py ~/PythonStuff/Python_Midterm/midterm_files/EnglishWords.txt ~/PythonStuff/Python_Midterm/midterm_files/Example_inputs/Example_inputs_program3 ~/PythonStuff/Python_Midterm/midterm_files/program3_outputs