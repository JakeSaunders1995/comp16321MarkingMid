import os
import sys

#morse Code decryption method. Input list of letters outputs word 
def decrypt_morseCode(lst):
	code = {".-": "a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", 
	"..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q",
	".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z",
	".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8",
	"----.":"9", "-----":"0", "--..--":", ", ".-.-.-":".", "..--..":"?", "-..-.":"/", "-....-":"-", "-.--.":"(", 
	"-.--.-":")", "-.-.-.":";", "---...":":", ".----.":"'", "..--.-": "_", ".-.-.":"+", "-...-":"=", "-.-.--":"!", '.-..-.':'"'}

	word = ""
	for letter in lst:
		word += code.get(letter)

	return word

#caesar +3 decryption method. Input word retuns word 
def decrypt_caesar(word):
	alph3= {"d":"a", "e":"b", "f":"c", "g":"d", "h":"e", "i":"f", "j":"g", "k":"h", "l":"i", "m":"j", "n":"k", "o":"l", "p":"m", 
	"q":"n", "r":"o", "s":"p", "t":"q", "u":"r", "v":"s", "w":"t", "x":"u", "y":"v", "z":"w", "a":"x", "b":"y", "c":"z", 
	".":".", ";":";", ",":",", "'":"'", '"':'"', "(":"(", ")":")", "4":"1", "5":"2", "6":"3", "7":"4", "8":"5", "9":"6", "0":"7", "1":"8", "2":"9"}

	result = ""
	for letter in word:
		result += alph3.get(letter)
	return result 

# hex decryptions method. Input lst of words
def decrypt_hex(lst):
	sentence = ""
	for number in lst:
		sentence += bytes.fromhex(number).decode("ASCII")

	sentence = sentence.lower()
		
	return sentence 




#Assigning the inputs 
input_Folder = sys.argv[1]
output_Folder = sys.argv[2]



#checks if output_folder exists, otherwise makes one n
if not os.path.isdir(output_Folder):
	os.mkdir(output_Folder)



#iterate over files in input_folder
for file in os.listdir(input_Folder):

	with open(os.path.join(input_Folder, file)) as file_in:
		phrase = file_in.read()
	
	char1 = phrase[0] #first letter in the document 
	sentence = ""
	index = phrase.find(":")  #finds the index of : to avoid including the name in the split() function 

	if char1 == "M":
		lst_of_words = phrase[index+1:].split("/")
		for word in lst_of_words:
			sentence +=  decrypt_morseCode(word.split()) + " "
		sentence = sentence[:-1]


	elif char1 == "C":
		lst_of_words = phrase[index+1:].split()
		for word in lst_of_words:
			sentence +=  decrypt_caesar(word.lower()) + " "
		sentence = sentence[:-1]
			
	elif char1 == "H":
		sentence = decrypt_hex(phrase[index+1:].split())

	with open(os.path.join(output_Folder, os.path.basename(file)[:-4] + "_f54617sa.txt"), "w") as file_out:
		file_out.write(sentence)





