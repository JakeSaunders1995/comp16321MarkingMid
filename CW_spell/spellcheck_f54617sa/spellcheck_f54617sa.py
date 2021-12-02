import sys 
import os


#Assigning the inputs 
englishWords = sys.argv[1]
input_Folder = sys.argv[2]
output_Folder = sys.argv[3]





# removes punctuation + numbers while incrementing values 
def remove(phrase):
	num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	pun = [ "!", "@", "#", "$", "%", "^",".",
	"&", "*", "(", ")", "_", "-", "+", "[", "]", "{", "}", ";", ":", "/", "'", '"', ",", "~", "`", "?"]

	global numbers
	global punctuations


	for ch in num:
		while ch in phrase:
			phrase = phrase.replace(ch, "", 1)
			numbers += 1

	for i in range(len(phrase)):
		if i <= (len(phrase)-3) and phrase[i:i+3] == "...":
			phrase = phrase.replace("...", "", 1)
			punctuations += 1

	for ch in pun:
		while ch in phrase:
			phrase = phrase.replace(ch, "", 1)
			punctuations += 1




	return phrase


#splits string into list of words/ increments uppercase letters 
def get_words(phrase):

	global uppercase

	lst_of_words = phrase.split()
	for i in range(len(lst_of_words)):
		temp = lst_of_words[i] 
		lst_of_words[i] = lst_of_words[i].lower()
		temp2 = lst_of_words[i]

		if temp != lst_of_words[i]:
			for j in range(len(temp)):
				if temp[j] != temp2[j]:
					uppercase += 1

	return lst_of_words


 




#checks if output_folder exists, otherwise makes one n
if not os.path.isdir(output_Folder):
	os.mkdir(output_Folder)

with open(englishWords) as dictionary:
	correctwords = dictionary.read().split()

#iterate over files in input_folder
for file in os.listdir(input_Folder):

	#initiating the variables 	
	uppercase = 0
	punctuations = 0
	numbers = 0
	words = 0
	correctW = 0
	incorrectW = 0

	with open(os.path.join(input_Folder, file)) as file_in:
		test = file_in.read()

	lst_words = get_words(remove(test))
	words = len(lst_words)

	for word in lst_words:
		if word in correctwords:
			correctW += 1


	incorrectW = words - correctW
	


	with open(os.path.join(output_Folder, os.path.basename(file)[:-4] + "_f54617sa.txt"), "w") as file_out:
		file_out.write("f54617sa" 
			+"\nFormatting ###################"
			+"\nNumber of upper case letters changed: " + str(uppercase)
			+"\nNumber of punctuations removed: " + str(punctuations)
			+"\nNumber of numbers removed: " + str(numbers)
			+"\nSpellchecking ###################"
			+"\nNumber of words: " + str(words)
			+"\nNumber of correct words: " + str(correctW)
			+"\nNumber of incorrect words: " + str(incorrectW))



