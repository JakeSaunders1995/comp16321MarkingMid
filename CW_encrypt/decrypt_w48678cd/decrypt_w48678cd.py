import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument(dest='argument1', help="This is the Input File")
parser.add_argument(dest='argument2', help="This is the Output File")

args = parser.parse_args()

FolderInput=args.argument1
FolderOutput=args.argument2

morse = {
  ".-": "a",
  "-...": "b",
  "-.-.": "c",
  "-..": "d",
  ".": "e",
  "..-.": "f",
  "--.": "g",
  "....": "h",
  "..": "i",
  ".---": "j",
  "-.-": "k",
  ".-..": "l",
  "--": "m",
  "-.": "n",
  "---": "o",
  ".--.": "p",
  "--.-": "q",
  ".-.": "r",
  "...": "s",
  "-": "t",
  "..-": "u",
  "...-": "v",
  ".--": "w",
  "-..-": "x",
  "-.--": "y",
  "--..": "z",
  "-----": "0",
  ".----": "1",
  "..---": "2",
  "...--": "3",
  "....-": "4",
  ".....": "5",
  "-....": "6",
  "--...": "7",
  "---..": "8",
  "----.": "9",
  ".-.-.-": ".",
  "--..--": ",",
  "..--..": "?",
  ".----.": "'",
  "-.-.--": "!",
  "-..-.": "/",
  "-.--.": "(",
  "-.--.-": ")",
  ".-...": "&",
  "---...": ":",
  "-.-.-.": ";",
  "-...-": "=",
  ".-.-.": "+",
  "-....-": "-",
  "..--.-": "_",
  ".-..-.": "\"",
  "...-..-": "$",
  ".--.-.": "@",
  "-..-": "×",
}

def De_morse(Morsecode):
	words=Morsecode.split(" ")
	decrp=""
	while "" in words:
		words.remove("")
	for n in range(0,len(words)):
		if words[n] == "/":
			decrp=decrp+" "
		else:
			try:
				decrp=decrp+morse[words[n]]
			except:
				print("unexpected code detected, unknown section ignored")
	return decrp

def De_caesar(Caesarcode):
	alphabet="xyzabcdefghijklmnopqrstuvwxyzabc"
	decrp=""
	for n in range(0,len(Caesarcode)):
		if Caesarcode[n] == " ":
			decrp=decrp+" "
		elif Caesarcode[n].isalpha()==False:
			print("non-alpha character ignored")
		else:
			alphabetPosition=3
			if Caesarcode[n].isupper():
				CaesarCharacter=Caesarcode[n].lower()
				print("upper case converted to lower case")
			else:
				CaesarCharacter=Caesarcode[n]
			while CaesarCharacter != alphabet[alphabetPosition]:
				alphabetPosition=alphabetPosition+1
			alphabetPosition=alphabetPosition - 3
			decrp=decrp + alphabet[alphabetPosition]
	return decrp

def De_hex(Hexcode):
	decrp=""
	words=Hexcode.split(" ")
	while "" in words:
		words.remove("")
	for n in range(0,len(words)):
		try:
			i=int(words[n], 16)
			decrp=decrp+chr(i)
		except:
			print("ignore non-Hex value")
	return decrp


for FileInput in os.listdir(FolderInput):
	In_fname=os.path.basename(FileInput)
	In_filepath = os.path.join(FolderInput, In_fname)

	fileIn, extension = os.path.splitext(FileInput)

	result=""
	enFile=open(In_filepath,"r")
	text=enFile.readline()
	text=text.strip()
	enFile.close()

	split=text.split(":")
	mode=split[0]
	code=split[1]

	if "Morse" in mode:
		result=De_morse(code)
	elif "Caesar" in mode:
		result=De_caesar(code)
	elif "Hex" in mode:
		result=De_hex(code)
	else:
		print("Error!")
	result=result.lower()
	Outfname=os.path.basename(FileInput)
	filename, file_extension = os.path.splitext(Outfname)
	fname=filename+"_w48678cd"+file_extension
	filepath = os.path.join(FolderOutput, fname)

	outFile=open(filepath,"w")
	outFile.write(result)
	outFile.close()

