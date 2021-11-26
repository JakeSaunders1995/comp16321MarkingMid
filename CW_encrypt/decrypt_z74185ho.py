import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("inputpath", type=str)
parser.add_argument("outputpath", type=str)
args = parser.parse_args()

cwd = os.getcwd()

def morse(thecode):
	sign = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
			'.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', 
			'...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
	
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
				'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	org_code = ""
	thecodeposition = 0

	while thecodeposition < len(thecode):
		thecodechar = thecode[thecodeposition]
		signposition = 0
		if (thecodechar == '/'):
			org_code += " "
		else:
			while (thecodechar != sign[signposition]):
				# print(signposition)
				signposition += 1
			org_code += alphabet[signposition]
		thecodeposition += 1

	return org_code

def caesar(thecode):
	alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
	
	org_code = ""
	thecodeposition = 0

	while thecodeposition < len(thecode):
		thecodeword = thecode[thecodeposition]
		for i in thecodeword:
			alphabetposition = 3
			while (i != alphabet[alphabetposition]):
				alphabetposition += 1
			alphabetposition -= 3
			org_code += alphabet[alphabetposition]
			# print(alphabetposition)
		org_code += " "
		thecodeposition += 1
	
	return org_code

def hex(thecode):
	org_code = ""
	thecodeposition = 0

	while thecodeposition < len(thecode):
		thecodechar = thecode[thecodeposition]
		i = int(thecodechar, 16)
		org_code += chr(i)
		thecodeposition += 1

	return org_code

for dirpath, dirnames, filenames in os.walk(args.inputpath):
	for file in filenames:
		if file.endswith(".txt"):
			targetfile = os.path.join(os.path.relpath(dirpath, cwd),file)
			with open(targetfile,'r') as f:
				line = f.read()
			code = line.replace(':', ' ').split()
			# print(code)

			morsecode = []
			caesarcode = []
			hexcode = []

			if (code[0] == 'Morse'):
				for i in code[2:]:
					morsecode.append(i)
					out = morse(morsecode)
			elif (code[0] == 'Caesar'):
				for i in code[2:]:
					caesarcode.append(i)
					out = caesar(caesarcode)
			elif (code[0] == 'Hex'):
				for i in code[1:]:
					hexcode.append(i)
					out = hex(hexcode)
			else:
				continue

			FileName = file.split(".")
			outputFileName = FileName[0] + "_z74185ho." + FileName[1]
			outputFilePath = os.path.join(args.outputpath, outputFileName)

			with open(outputFilePath, "w") as of:
				of.write(out)

			continue

		else:
			continue



