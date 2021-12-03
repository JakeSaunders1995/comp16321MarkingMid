import sys 
import os 


morse_code = {".-" : "a", "-..." : "b", "-.-." : "c", "-.." : "d", "." : "e", 
				"..-." : "f", "--." : "g", "...." : "h", ".." : "i", ".---" : "j",
				"-.-" : "k", ".-.." : "l", "--" : "m", "-." : "n", "---" : "o",
				".--." : "p", "--.-" : "q", ".-." : "r", "..." : "s", "-" : "t", 
				"..-" : "u", "...-" : "v", ".--" : "w", "-..-" : "x", "-.--" : "y",
				"--.." : "z", ".----" : "1", "..---" : "2", "...--" : "3", "....-" : "4",
				"....." : "5", "-...." : "6", "--..." : "7", "---.." : "8", "----." : "9"}

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]

if os.path.exists(outputFolder) == False:
	os.makedirs(outputFolder)

for input_file in os.listdir(inputFolder):
	plain_text = ""
	cipher_text = 0 

	file = open(os.path.join(inputFolder,input_file), "r")

	file_body = file.read()
	contents = file_body.split(":")
	file.close()


	if contents[0] == "Hex":
		cipher_text = contents[1].split()

		for hex_number in cipher_text:
			decimal_number = int(hex_number, 16)
			character = chr(decimal_number)
			plain_text = plain_text + character

	elif "Caesar" in contents[0]:

		cipher_text = contents[1]

		for character in cipher_text:

				ascii_value = ord(character)
				ascii_value = ascii_value - 3 


				if ascii_value == 29:
					ascii_value = 32

				elif ascii_value < 97:
					ascii_value = ascii_value + 26 
				
					


				plain_text = plain_text + chr(ascii_value)

	else:

		cipher_text = contents[1].split("/")

		for word in cipher_text: 
			character = word.split()


			for letter in character: 
				alphacharacter = morse_code.get(letter)

				plain_text = plain_text + alphacharacter

			plain_text = plain_text + " "

	name, ext = os.path.splitext(input_file)
	output_file = name + "_h64411rs" + ext 

	file = open(os.path.join(outputFolder, output_file), "w")
	file.write(plain_text)
	file.close()
	




