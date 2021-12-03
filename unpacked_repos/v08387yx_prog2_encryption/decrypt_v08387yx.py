import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def filelist(input_file):
	file_path_list = []
	for file in os.listdir(input_file):
		file_path = os.path.join(input_file,file)
		file_path_list.append(file_path)
	return(file_path_list)

l = filelist(args.input_file)
dict = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o",".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v",".--":"w", "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0", "/":" "}
alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
for name in l:
	f_input = open(name)
	ciphertext = f_input.read()
	plain_text =""
	if ciphertext[0] == "M":
		c = ciphertext[11:len(ciphertext)].split(" ")		
		for text in c:
			if text != "\n":
				plaintext = dict[text]
			else:
				plaintext = ""
			plain_text = plain_text + plaintext
	elif ciphertext[0] == "C":
		c = list(ciphertext[18:len(ciphertext)])
		for text in c:
			if text != " " and text != "\n":
				text = text.lower()
				alphabetPosition = 3
				while text != alphabet[alphabetPosition]:
					alphabetPosition += 1
					pass
				plaintext = alphabet[alphabetPosition-3]	
			elif text == "\n":
				plaintext = ""
			elif text == " ":
				plaintext = " "
			plain_text = plain_text + plaintext
	elif ciphertext[0] == "H":
		c = ciphertext[4:len(ciphertext)].split(" ")
		for text in c:
			if text != "\n":
				plaintext = chr(int(text,16))
				plaintext = plaintext.lower()
			else:
				plaintext = ""
			plain_text = plain_text + plaintext
	f_input.close()
	basename = os.path.basename(name)
	filename = basename.split(".txt")
	filename.append("_v08387yx.txt")
	file_name = ''.join(filename)
	output_file_name = os.path.join(args.output_file,file_name)
	f_output = open(output_file_name,"w")
	f_output.write(plain_text)
	f_output.close()