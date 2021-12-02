#Decrypt_v0
import os
import re
import argparse

#Get input&outpus file path from command line.
parser = argparse.ArgumentParser(description = 'Please enter file path')
parser.add_argument('param1', type = str, help = 'absolute input file path')
parser.add_argument('param2', type = str, help = 'absolute output file path')
args = parser.parse_args()

Input_Files = os.listdir(args.param1)

Morse_Code = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', 
'--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', 
'-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', 
'...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', 
'.----':'1', '..---':'2', '...--':'3', 
'....-':'4', '.....':'5', '-....':'6', 
'--...':'7', '---..':'8', '----.':'9', 
'-----':'0'}


def Morse_Decode(string, sign):
	plaintext = ""
	plainWord = ""
	lists = string.split(sign)
	count = 0
	for code in lists:
		cipherWord = lists[count]
		count += 1
		cipherChar = cipherWord.split(" ")
		while "" in cipherChar:
			cipherChar.remove("")
		for char in cipherChar:
			if char not in Morse_Code:
				print("Couldn't find " + char)
			elif char in Morse_Code:
				plainChar = Morse_Code[char]
				plainWord += plainChar
		plaintext += plainWord + " "	
		plainWord = ""
	return(plaintext)

a = 0
for file in Input_Files:
	if not os.path.isdir(file):
		f = open(args.param1+'/'+file)
		content = f.read()
		f.close()

	#Decide methods to decrypt
		if 'Hex' in content:
			plaintext = ""
			RemoveTitle = content.replace("Hex:", "")
			Strip = RemoveTitle.replace(" ", "")
			count = 0
			header = '0x'
			result = []
			bus = header
			for i in Strip:
				count += 1
				if count == 1:
					bus += i
				elif count == 2:
					count = 0
					bus += i
					result.append(bus)
					bus = header
			for i in result:
				plaintext += chr(int(i,base=16))


		elif 'Caesar Cipher' in content:
			plaintext = ""
			RemoveTitle = content.replace("Caesar Cipher(+3):", "")
			cipherText = RemoveTitle.lower()
			for i in range(len(cipherText)):
				char = cipherText[i]	
				if ord('a') <= ord(char) <= ord('c'):
					plaintext += chr(ord(char) + 23)
				elif ord('d') <= ord(char) <= ord('z'):
					plaintext += chr((ord(char) - 3))
				elif char == " ":
					plaintext += char
				else:
					continue 

		elif "Morse Code" in content:
			cipherText = content.replace("Morse Code:", "")
			count = 0

			if __name__ == "__main__":
				plaintext = (Morse_Decode(cipherText, "/"))

		output = open(args.param2 + "/" + (Input_Files[a])[:-4] + "_m56135cw.txt",'w')
		a += 1
		output.write(plaintext.strip().lower())
		output.close()



