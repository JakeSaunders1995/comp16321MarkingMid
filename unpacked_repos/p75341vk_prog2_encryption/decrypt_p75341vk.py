import argparse
import os

def decrypt(line):
	plaintext = ""
	if (line.startswith(cipher[0]) == True):
		ciphertext = line[len(cipher[0])::].split()
		for hexnum in ciphertext:
			num = int(hexnum, 16)
			character = chr(num)
			plaintext = plaintext + character

	elif (line.startswith(cipher[1]) == True):
		for pos in range(len(cipher[1]), len(line)):
			if line[pos] != " " and line[pos]!="\n":
				cipherchar = line[pos]
				if cipherchar not in ('a','b','c','A','B','C'):
					ciphernum = ord(cipherchar)
					plainnum = ciphernum - 3
					character = chr(plainnum)				
				else:
					if cipherchar == 'a' or cipherchar =='A':
						character = 'x'
					elif cipherchar == 'b' or cipherchar =='B':
						character = 'y'
					elif cipherchar == 'c' or cipherchar =='C':
						character = 'z'
				plaintext = plaintext + character
			elif line[pos]==" ":
				plaintext += " "

	elif (line.startswith(cipher[2]) == True):
		ciphertext = line[len(cipher[2])::].split()
		for cipherword in ciphertext:
			character = str(morse.get(cipherword))
			plaintext = plaintext + character
	return plaintext

parser = argparse.ArgumentParser() 	# initialing parser
parser.add_argument('inputFolder') 	# inputting input folder from command line
parser.add_argument('outputFolder') 
folders = parser.parse_args() 		# passing the parameters
	
inputpath = folders.inputFolder		#assigning the path of the input folder to the variable inputpath
outputpath = folders.outputFolder
inputDir = os.listdir(inputpath) # stores the list of files in the input folder to inputDir
outputDir = os.listdir(outputpath)
cipher = ["Hex:", "Caesar Cipher(+3):", "Morse Code:"]
morse = {
	".-":"A",
	"-...":"B",
	"-.-.":"C",
	"-..":"D",
	".":"E",
	"..-.":"F",
	"--.":"G",
	"....":"H",
	"..":"I",
	".---":"J",
	"-.-":"K",
	".-..":"L",
	"--":"M",
	"-.":"N",
	"---":"O",
	".--.":"P",
	"--.-":"Q",
	".-.":"R",
	"...":"S",
	"-":"T",
	"..-":"U",
	"...-":"V",
	".--":"W",
	"-..-":"X",
	"-.--":"Y",
	"--..":"Z",
	".----":"1",
	"..---":"2",
	"...--":"3",
	"....-":"4",
	".....":"5",
	"-....":"6",
	"--...":"7",
	"---..":"8",
	"----.":"9",
	"-----":"0",
	"/":" ",
	"-.-.--":"!",
	".--.-.":"@",
	"...-..-":"$",
	".-...":"&",
	"-.--.":"(",
	"-.--.-":")",
	".-.-.-":".",
	"--..--":",",
	"..--..":"?",
	"---...":":",
	"-.-.-.":";",
	"-....-":"-",
	".----.":"'",
	".-..-.":'"',
}

for inputfilename in inputDir:
	inputtext = os.path.join(inputpath,inputfilename) # creating the path of the input file
	if os.path.isfile(inputtext) and inputfilename.endswith(".txt"):
		with open(inputtext) as inputfile:
			text = inputfile.readline()
			text = text.strip()
			finaltext = decrypt(text)
			finaltext = finaltext.lower()

		outputfilename = inputfilename.replace('.txt', "") + "_p75341vk.txt" # creating the output file name from the input file name
		outputtext = os.path.join(outputpath,outputfilename) # creating the path of the output file

		if (outputfilename not in outputDir): # to check if the file is present or not
			outputfile = open(outputtext, "x") # create file, if not present
		else:
			outputfile = open(outputtext, "w") # write to existing file, if present
		outputfile.write(finaltext)
		outputfile.close()
		inputfile.close()