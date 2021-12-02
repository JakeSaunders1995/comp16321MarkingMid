import os, sys

input_folder = sys.argv[1]
output_folder = sys.argv[2]
dir_list = os.listdir(input_folder)
print(dir_list)

x = 0
y = 4



for x in range (x, len(dir_list),1):
	file = open(input_folder +"/"+ dir_list[x])
	mylist=file.readline()
	print(mylist)
	if mylist[0] == "H":
		data = mylist[4: len(mylist)]
		hexa = bytes.fromhex(data)
		ascii_text = hexa.decode("ASCII")
		print (ascii_text)
		output_file = dir_list[2].replace("txt","_m65670fa.txt")
		output_file=output_folder+"/"+output_file
		with open (output_file, "a")as file:
			file.write(f'{ascii_text}')

	elif mylist[0] == "C":
		orginalText = mylist[18: len(mylist)]
		output = ""
		cipherTextPosition = 0
		while cipherTextPosition < len(orginalText):
			cipherTextChar = orginalText[cipherTextPosition]
			ASCIIValue = ord(cipherTextChar)
			ASCIIValue -= 3
			output += chr(ASCIIValue)
			if orginalText[cipherTextPosition]==" ":
				output = output + " "
			cipherTextPosition += 1
		print(output)
		output_file = dir_list[0].replace("txt","_m65670fa.txt")
		output_file=output_folder+"/"+output_file
		with open (output_file, "a")as file:
			file.write(f'{output}')
	elif mylist[0] == "M":
		morse = mylist[11:]
		morse_text = {
   		 '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
		}
		text = ""
		for j in morse:
			if j != ' ':
				text += j
				if j not in morse_text:
					print("no data formatted")
					break
			elif j == '/':
				print(morse_text[text], end=' ')
			else:
				print(morse_text[text], end='')
				output_file = dir_list[1].replace("txt","_m65670fa.txt")
				output_file=output_folder+"/"+output_file
				with open (output_file, "a")as f:
					f.write(f'{morse_text[text]}')
					text = ''





