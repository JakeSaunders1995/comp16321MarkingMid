import os, argparse, re
parser = argparse.ArgumentParser()
parser.add_argument('x', type = str)
parser.add_argument('y', type = str)
args = parser.parse_args()
def translator(file_111):
	file_output_ = file_111[0:(len(file_111) - 4)] + "_y48052as" + ".txt"
	file_output_ = args.y + file_output_
	file_111 = args.x + file_111
	file1 = open(file_111)
	file2 = open(file_output_, "w")
	s1 = file1.read()
	position = s1.find(':')
	encryption = s1[0]
	s1 = s1[int(position+1):len(s1)]
	'''print(encryption)'''
	'''print(s1)'''
	def translate_hexadecimal(s_hex):
		s_hex = s_hex.split()
		for split in s_hex:
			split = bytes.fromhex(split).decode()
			file2.write(split.rstrip('\n'))



	def morse(s_check):
		if(s_check == "-."):
			return "a"
		elif(s_check == "-..."):
			return "b"
		elif(s_check == "-.-."):
			return "c"
		elif(s_check == "-.."):
			return "d"
		elif(s_check == "."):
			return "e"
		elif(s_check == "..-."):
			return "f"
		elif(s_check == "..-"):
			return "g"
		elif(s_check == "...."):
			return "h"
		elif(s_check == ".."):
			return "i"
		elif(s_check == ".---"):
			return "j"
		elif(s_check == "-.-"):
			return "k"
		elif(s_check == ".-.."):
			return "l"
		elif(s_check == "--"):
			return "m"
		elif(s_check == "-."):
			return "n"
		elif(s_check == "---"):
			return "o"
		elif(s_check == ".--."):
			return "p"
		elif(s_check == "--.-"):
			return "q"
		elif(s_check == ".-."):
			return "r"
		elif(s_check == "..."):
			return "s"
		elif(s_check == "-"):
			return "t"
		elif(s_check == "..-"):
			return "u"
		elif(s_check == "...-"):
			return "v"
		elif(s_check == ".--"):
			return "w"
		elif(s_check == "-..-"):
			return "x"
		elif(s_check == "-.--"):
			return "y"
		elif(s_check == "--.."):
			return "z"
		elif(s_check == "-----"):
			return "0"
		elif(s_check == ".----"):
			return "1"
		elif(s_check == "..---"):
			return "2"
		elif(s_check == "...--"):
			return "3"
		elif(s_check == "....-"):
			return "4"
		elif(s_check == "....."):
			return "5"
		elif(s_check == "-...."):
			return "6"
		elif(s_check == "--..."):
			return "7"
		elif(s_check == "---.."):
			return "8"
		elif(s_check == "----."):
			return "9"
		else:
			return " "


	def translate_morse(s_encode):
		word = ""
		for character in s_encode:
			if (character != "/"):
				word += character
			else:
				code = word.split()
				for split in code:
					file2.write(morse(split))
				word = ""
				file2.write(" ")






	def encoder(c1):
		if(ord(c1) - 3 < 97):
			return (chr((ord(c1) - 3) + 26))
		else:
			return (chr(ord(c1) - 3))



	def translate_Caeser_Cipher(s_Caeser_Cipher_):
		for i in s_Caeser_Cipher_:
			if(i != " "):
				file2.write(encoder(i))
			elif(i == " "):
				file2.write(" ")
			else:
				file2.write(i)





	if(encryption == "H"):
		translate_hexadecimal(s1)
	elif(encryption == "M"):
		translate_morse(s1)
	else:
		translate_Caeser_Cipher(s1)

	file1.close()
	file2.close()

for file in os.listdir(args.x):
	translator(file)	