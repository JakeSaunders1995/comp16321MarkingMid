import argparse
import os

def outputResult(a):
	file_name= s.replace(".txt","_e54842zt.txt")
	output_file=open(output_folder_path+"/"+file_name, "w")
	output_file.write(a)
def indir():
	inputDir = sorted(os.listdir(args.inputfolder))
	return inputDir
my_parser = argparse.ArgumentParser()
my_parser.add_argument('inputfolder', help="input")
my_parser.add_argument('outputfolder', help="output")
args = my_parser.parse_args()
input_folder_path=args.inputfolder
output_folder_path=args.outputfolder

x = indir()

for s in x:

	encrypted_file=open(input_folder_path+"/"+s, "r")
	encryptedFile= encrypted_file.read()
	encrypted_file.close()

	index=0
	number="0123456789abcdefABCDEF"

	if encryptedFile[index]=="H" or encryptedFile[index]=="h":
		result=""
		storageNum=""
		file=encryptedFile[4:]
		for i in file:
			if i in number:
				storageNum+=i
			if i==" ":
				result+=chr(int(storageNum,16))
				storageNum=""
		result+=chr(int(storageNum,16))
		result=result.lower()
		outputResult(result)

	if encryptedFile[index]=="C" or encryptedFile[index]=="C":
		file=encryptedFile[18:]
		alphabet='abcdefghijklmnopqrstuvwxyz'
		distance=3	
		decrypt=''
		for j in file:
			if j ==" ":
				decrypt+=" "
			elif j =="\n":
				decrypt+=""
			else:
				position=alphabet.find(j)
				new_position=(position-distance)%26
				decrypt+=alphabet[new_position]
		outputResult(decrypt)

	MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
	    'C':'-.-.', 'D':'-..', 'E':'.',
	    'F':'..-.', 'G':'--.', 'H':'....',
	    'I':'..', 'J':'.---', 'K':'-.-',
	    'L':'.-..', 'M':'--', 'N':'-.',
	    'O':'---', 'P':'.--.', 'Q':'--.-',
	    'R':'.-.', 'S':'...', 'T':'-',
	    'U':'..-', 'V':'...-', 'W':'.--',
	    'X':'-..-', 'Y':'-.--', 'Z':'--..',
	    '1':'.----', '2':'..---', '3':'...--',
	    '4':'....-', '5':'.....', '6':'-....',
	    '7':'--...', '8':'---..', '9':'----.',
	    '0':'-----', ', ':'--..--', '.':'.-.-.-',
	    '?':'..--..', '/':'-..-.', '-':'-....-',
	    '(':'-.--.', ')':'-.--.-'
	 }

	if encryptedFile[index]=="M" or encryptedFile[index]=="m":
		var=""
		mor=""
		file=encryptedFile[11:]
		file+=" "
		for m in file:
			if m =="." or m =="-":
				var+=m
			elif m ==" ":
				for a,b in MORSE_CODE_DICT.items():
					if b==var:
						mor+=a
						var=""
			elif m =="/":
				mor+=" "
		MOR=mor.lower()
		outputResult(MOR)