import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", type=str)
parser.add_argument("output_dir", type=str)
args = parser.parse_args()

if args.input_dir[:-1] != "/":
	args.input_dir += "/"
	
if args.output_dir[:-1] != "/":
	args.output_dir += "/"


def caesar(text):
	letters = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	words = text.split(" ")
	result = ""
	
	for i in range(len(words)):
		new_word = ""
		for j in range(len(words[i])):
			char = words[i][j]
			if char in letters:
				letters_index = len(letters)-1
				while char != letters[letters_index]:
					letters_index -= 1
				char = letters[letters_index - 3]
			new_word += char
		result += new_word
		if i < len(words)-1:
			result += " "
			
	return result.lower()
	

def hexadecimal(text):
	hex_values = {"a":10, "b":11, "c":12, "d":13 ,"e":14, "f":15}
	chars = text.split(" ")
	result = ""
	
	for char in chars:
		char_values = []
		ASCII_value = 0
		for i in range(len(char)):
			if char[i] in ["a", "b", "c", "d", "e", "f"]:
				char_values.append(hex_values.get(char[i]))
			elif char[i].isnumeric():
				char_values.append(int(char[i]))
			else:
				char_values.append(0)
			
			ASCII_value += char_values[i]*(16**(len(char)-i-1))
		
		if ASCII_value >= 0 and ASCII_value <= 255:
			result += chr(ASCII_value)
		
	return result.lower()
		

def morse_code(text):
	morse_code = {"/":" ", ".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0", ".-.-.-":".", "--..--":",", "..--..":"?", "-.-.--":"!", ".----.":"\'", "-..-.":"/", "---...":":", "-.-.-.":";", ".-.-.":"+", "-....-":"-", "-...-":"=", "-.--.":"(", "-.--.-":")", "..--.-":"_", ".-..-.":"\"", ".-...":"&", ".--.-.":"@"}
	chars = text.split(" ")
	result = ""
	
	for char in chars:
		result += str(morse_code.get(char))
	
	return result.lower()
	

def decrypt(data):
	data = data.split(":")
	if len(data) != 2:
		return ""
	
	algorithm = data[0].lower()
	text = data[1].lower()
	output = ""
	
	if algorithm == "caesar cipher(+3)":
		output = caesar(text)
		
	elif algorithm == "hex":
		output = hexadecimal(text)

	elif algorithm == "morse code":
		output = morse_code(text)
	
	return output


if not os.path.isdir(args.output_dir):
	os.makedirs(args.output_dir)
	
file_list = os.listdir(args.input_dir)

for x in file_list:
	if x[-4:] == ".txt":
		with open(args.input_dir + x) as f:
			result = decrypt(f.read().replace("\n", ""))
			with open(args.output_dir + x[:-4] + "_y99614zh.txt", "w") as g:
				g.write(str(result))



