import argparse
import os

input_dir=[]# input files list

morse = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d",
".":"e", "..-.":"f", "--.":"g",
"....":"h", "..":"i", ".---":"j", "-.-":"k",
".-..":"l", "--":"m", "-.":"n",
"---":"o", ".--.":"p", "--.-":"q",
".-.":"r", "...":"s", "-":"t",
"..-":"u", "...-":"v", ".--":"w",
"-..-":"x", "-.--":"y", "--..":"z",
"-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
".-.-.-":".", "..--..":"?", "-.-.--":"!","---.":"!","--..--":",","---...":":","-.-.-.":";",
"-....-":"-", "..--.-":"_", "-.--.": "(", "-.--.-":")", ".----.":"'", "-...-":"=", "-..-.": "/",  
}


def ChangePath(path):# add /
	if path[-1]!="\\" or path[-1]!="/":
		path+="/"
	return path

def Hex(cipher,List):
	List=cipher.split(" ")
	plain=""
	for char in List:
		if char!="\n":
			plain+=chr(int(char, 16))
	return plain

def CaesarCipher(cipher,List):
	List=cipher.split(" ")
	plain=""
	for char in List:
		for sin_char in char:
			if sin_char!="\n":
				ASVal=ord(sin_char)
				ASVal-=3
				if ASVal<97:
					ASVal+=26
				plain+=(chr(ASVal))
		plain+=" "
	plain=plain[0:-1]
	return plain

def MorseCode(cipher,List,dictionary):
	List=cipher.split(" ")
	plain=""
	for char in List:
		if char!="\n":
			if char=="/":
				plain+=" "
			else:
				plain+=dictionary[char]
	return plain

parser=argparse.ArgumentParser()
parser.add_argument("inputFile", type=str)
parser.add_argument("outputFile", type=str)
args=parser.parse_args()

input_folder=ChangePath(args.inputFile)
output_folder=ChangePath(args.outputFile)

input_dir = os.listdir(input_folder)

#os.chdir(input_folder)# change to that path

print("There are "+str(len(input_dir))+" files in the input_folder.\n")

for file in input_dir:
	cipherList=[]
	plainText=""
	mark_file= open(input_folder+file, "r")
	content=mark_file.read()
	colonPosition=content.index(":")

	if content[0:colonPosition]=="Hex":
		plainText=Hex(content[colonPosition+1:],cipherList)

	elif content[0:colonPosition]=="Caesar Cipher(+3)":
		plainText=CaesarCipher(content[colonPosition+1:],cipherList)

	else:
		plainText=MorseCode(content[colonPosition+1:],cipherList,morse)

	mark_file.close()


	result=open(output_folder+file[0:-4]+"_j59004hl.txt", "w")
	result.write(plainText.lower())
	result.close()
print("(The plain text result has saved into the output folder)\n")