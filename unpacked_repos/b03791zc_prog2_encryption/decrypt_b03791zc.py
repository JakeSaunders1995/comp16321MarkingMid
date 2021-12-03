import argparse 
import os

path = argparse.ArgumentParser()
path.add_argument("input_path")
path.add_argument("output_path")

file = path.parse_args()
for infiles in os.listdir(file.input_path):
	Input = open(file.input_path + "/" +infiles, "r")
	t = list(file.output_path + "/" +infiles)
	for i in range (4):
		t.pop(-1)
	t = ("").join(t)
	filename = t + "_b03791zc"
	filepath = os.path.join(file.output_path, filename)
	Output = open(filepath, "w")

	encryp = Input.readlines()
	encryp_s = encryp[0].split(":")
	decryp = []
	if encryp_s [0] == "Hex":
		txt = encryp_s[1].split()
		for char in range (len(txt)):
			decryp.append(chr(int(txt[char], 16)))
		decryp = "".join(decryp)
		Output.writelines(decryp.lower())
	elif encryp_s [0] == "Caesar Cipher(+3)":
		txt = list(encryp_s[1])
		for char in range (len(txt)):
			if txt[char] == " ":
				decryp.append(txt[char])
			elif txt[char] == "\n":
				pass
			elif txt[char] != " ":
				c = ord(txt[char])
				for i in range (3):
					c -= 1
					if c < 97:
						c = 122
				decryp.append(chr(c))
		decryp = "".join(decryp)
		Output.writelines(decryp.lower())
	elif encryp_s [0] == "Morse Code":
		morse_lib = {"/": " ", ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0", "--..--": ", ", ".-.-.-": ".", "..--..": "?", "-..-.": "/", "-....-": "-", "-.--.": "(", "-.--.-": ")"}
		txt = encryp_s[1].split(" ")
		for char in range (len(txt)):
			decryp.append(morse_lib[txt[char]])
		decryp = "".join(decryp)
		Output.writelines(decryp.lower())
		Input.close()
		Output.close()