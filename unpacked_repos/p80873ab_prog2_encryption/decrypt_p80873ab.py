import sys
import os
folder_output= sys.argv[2]
folder_input = sys.argv[1]

if not os.path.isdir(folder_output):
	os.mkdir(folder_output)

for file in os.listdir(folder_input):
	with open(os.path.join(folder_input,file),"r") as file_input:
		inputstr=file_input.read()
		inputstr+=" "

		for i in range(len(inputstr)):
			if inputstr[i]==":":
				break
		type=inputstr[:i]

		def Hex(inputstr):
			temp=0
			list=inputstr[4:].split()
			final=""
			for i in range(len(list)):
				list[i]=bytes.fromhex(list[i])
				final=final+list[i].decode("ASCII")
			return final

		def CaesarCipher(inputstr):
			extra={'a':'x','b':'y','c':'z','0':'7','1':'8','2':'9'}
			text=inputstr[18:].split()
			final=""
			for j in range(len(text)):
				for i in text[j]:
					if i==" ":
						final+=" "
					elif i=="a" or i=="b" or i=="c" or i=="0" or i=="1" or i=="2":
						for k in extra:
							if i==k:
								final+=extra[i]

					else:
						final+=chr(ord(i)-3)
				final=final[:len(final)-1]

			return final

		def morseCode(inputstr):

			final=""
			char={'.-':'a', '-...':'b','-.-.':'c', '-..':'d', '.':'e','..-.':'f', '--.':'g', '....':'h','..':'i',
					'.---':'j', '-.-':'k','.-..':'l', '--':'m',
					'-.':'n','---':'o', '.--.':'p', '--.-':'q',
					'.-.':'r', '...':'s', '-':'t','..-':'u',
					'...-':'v', '.--':'w','-..-':'x', '-.--':'y',
					'--..':'z','.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':',', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')','-.-.--':'!',
                    '---...':':','-.-.-.':';',".----.":"'",'.-..-.':'"'}
			list=inputstr[11:].split("/")
			for i in range(len(list)):
				list[i]=list[i].split()
				for j in range(len(list[i])):
					final+=char[list[i][j]]
				final+=" "
			final=final[:len(final)-1]
			return final


		if type=="Morse Code":
			result=morseCode(inputstr)

		elif type=="Caesar Cipher(+3)":
			result=CaesarCipher(inputstr)

		else:
			result=Hex(inputstr)
		result=result.lower()
	with open(os.path.join(folder_output,os.path.basename(file)[:-4]+"_p80873ab"),"w") as file_output:
		file_output.write(result)