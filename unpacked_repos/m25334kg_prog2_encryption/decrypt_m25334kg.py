import argparse
import re
import os

try:
	parser=argparse.ArgumentParser()
	parser.add_argument("input_folder",help="folder containing files with cipher-text", type=str)
	parser.add_argument("output_folder",help="folder containing files with decoded text", type=str)
	folders=parser.parse_args()

	fol_in=folders.input_folder
	fol_out=folders.output_folder

	input_files=os.listdir(fol_in)

	for file in input_files:
		f_in=open(fol_in+ "/" + file)
		output_file= file.rstrip(".txt") + "_m25334kg" + ".txt"
		f_out=open(fol_out+"/"+output_file, "w")
		cipher=f_in.read()
		cipherList=cipher.split(":")

		method=cipherList[0]
		text=cipherList[1]

		if "morse" in method or "Morse" in method:
			string=""
			morseChar={"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".","f":"..-.", "g":"--.","h":"....", "i":"..","j":".---","k":"-.-", "l":".-..","m":"--","n":"-.", "o":"---","p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-","y":"-.--","z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--","4":"....-","5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", ",":"--..--", ".":".-.-.-", "?":"..--..", ";":"-.-.-.", ":":"---...", "/":"-..-.", "-":"-....-", "'":".----.", '"':".-..-.", "(":"-.--.", ")":"-.--.-", "=":"-...-", "+":".-.-.", "@":".--.-.", "!":"-.-.--", "&":".-..."}
			words=text.split("/")
			for word in words:
				alphabets=word.split()
				curWord=""
				for i in alphabets:
					for key in morseChar:
						if morseChar[key]==i:
							alpha=key
							curWord+=alpha
				string+=curWord+" "


		elif re.search("^caesar",method) or re.search("^Caesar",method,):
			string=""
			for i in text:
				if i==" " or i=="\n":
					string+=i 
				elif i=="a" or i=="A":
					string+="x"
				elif i=="b" or i=="B":
					string+="y"
				elif i=="c" or i=="C":
					string+="z"
				elif i=="0":
					string+="7"
				elif i=="1":
					string+="8"
				elif i=="2":
					string+="9"
				else:
					Ascii=ord(i)-3
					char=chr(Ascii)
					if char.isupper():
						char=char.lower()
					string+=char

		elif re.search("^Hex",method) or re.search("^hex",method):
			hexArray=bytes.fromhex(text)
			hexWord=hexArray.decode("ascii")
			string=""
			for i in hexWord:
				if i.isupper():
					string+=i.lower()
				else:
					string+=i
			
		else:
			string="Could not decode string."


		f_out.write(string)
		f_in.close()
		f_out.close()

except SyntaxError as error:
	print(error)

except Exception:
	print("Oops! Couldn't decode string.")