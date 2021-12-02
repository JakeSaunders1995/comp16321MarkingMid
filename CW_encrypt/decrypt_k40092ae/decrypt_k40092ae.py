import os
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("readme", help="rugby scoring program")
parser.add_argument('input_folder_path')
parser.add_argument('output_folder_path')
args = parser.parse_args()
#print(args.file)

args = parser.parse_args()

inputfolpath = (args.input_folder_path)
outputfolpath = (args.output_folder_path)

def convertHex(hex):
		temp = list(hex)
		hexlist = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
		decsum = (16 * hexlist.index(temp[0])) + hexlist.index(temp[1]) 
		return decsum

def convertMorse(morse):
	finalstring = ""
	morsecodeoptions = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--....","---..","----.","-----",".-.-.-","..--..","-.-.--","--..--","---...","-.-.-.","-.--.","-.--.-",".----.",".-..-.","..--.-","-....-"]
	alphabetandnumbers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','.','?','!',',',':',';','(',')',"'",'"','–','-']
	for count in range(len(morse)):
		if morse[count] in morsecodeoptions:
			finalstring = finalstring + alphabetandnumbers[morsecodeoptions.index(morse[count])]
		else:
			finalstring = finalstring + " "


	return (finalstring)

def convertCaesar(cipher):
	cipher = cipher.lower()
	temp = list(cipher)
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	new = ""
	for count in range(len(temp)):
		if temp[count] in alphabet:
			indexpos = alphabet.index(temp[count])
			if indexpos < 3:
				indexpos = indexpos + 26
			new = new + alphabet[indexpos-3]
		else:
			new = new + temp[count]
	return new



for filename in os.listdir(inputfolpath):
	inputfile = open(inputfolpath + "/" + filename,"r")
	line = inputfile.readline()
	container = line.split(":")
	#print (container)
	temp = filename.split(".")
	username = 'k40092ae'
	
	output_file_name = temp[0] +"_"+ username + "." + temp[1] 
	

	decimallist = []

	if container[0] == "Hex":
		characterlist = container[1].split(" ")
		for j in range(len(characterlist)):
			decimallist.append(chr(convertHex(characterlist[j])))
		x = "".join(decimallist)
	elif container[0] == "Morse Code":
		characterlist = container[1].split(" ")
		x = convertMorse(characterlist)
	elif container[0] == "Caesar Cipher(+3)":
		characterlist = container[1]
		#print (characterlist)
		x = convertCaesar(characterlist)
		
	x = x.lower()


	#print (x)
	outputfile = open(outputfolpath+ "/" + output_file_name,"w")
	outputfile.write(x)