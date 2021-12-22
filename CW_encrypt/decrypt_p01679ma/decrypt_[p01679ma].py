import os
import sys

input_folder = sys.argv[1]
output_folder = sys.argv[2]
dir_list = os.listdir(input_folder)
print(dir_list)

i = 0


for i in range (i, len(dir_list),1):
	file = open(input_folder +"/"+ dir_list[i])
	print("\n")
	list1=file.readline()
	print(list1)
	if list1[0] == "H":
		hexacode = list1[4: len(list1)]
		hexacode1 = bytes.fromhex(hexacode)
		asciicode = hexacode1.decode("ASCII")
		print (asciicode)
		output_file = dir_list[2].replace("txt","_p01679ma.txt")
		output_file=output_folder+"/"+output_file
		with open (output_file, "a")as file:
			file.write(f'{asciicode}')

	elif list1[0] == "C":
		Caesar = list1[18: len(list1)]
		Text = ""
		i = 0
		while i < len(Caesar):
			text1 = Caesar[i]
			ASCII = ord(text1)
			ASCII -= 3
			Text += chr(ASCII)
			if Caesar[i]==" ":
				Text = Text + " "
			i += 1
		print(Text)
		output_file = dir_list[0].replace("txt","_p01679ma.txt")
		output_file=output_folder+"/"+output_file
		with open (output_file, "a")as file:
			file.write(f'{Text}')

	elif list1[0]=="M":
		Morse = list1[11:]
		Morsecode= {
   		 '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
		}
		words = ''
		for i in (Morse):
			if i != ' ':
				words=words+i
				if i not in Morsecode:
					print ('data not formatted')
					break
			elif i == '/':
				print(Morsecode[words], end=' ')
			else: 
				print(Morsecode[words], end='') 
				output_file = dir_list[1].replace("txt","_p01679ma.txt")
				output_file=output_folder+"/"+output_file
				with open (output_file, "a")as file:
					file.write(f'{Morsecode[words]}')
					words = ''


	

		
    



