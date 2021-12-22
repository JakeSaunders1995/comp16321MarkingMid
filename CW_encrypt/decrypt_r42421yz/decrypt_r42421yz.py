import argparse, os, sys, re

h = "h"
H = "H"
c = "c"
C = "C"
m = "m"
M = "M"

filepath = sys.argv[1]
outputfilepath = sys.argv[2]
os.mkdir(outputfilepath)

inputfile = os.listdir(filepath)
print(inputfile)
for file in inputfile:

	os.chdir(outputfilepath)
	outputfilename = 'text_file' + file[9] + '_r42421yz.txt'
	fp = open(outputfilename,'w')




	inputfilepath = os.path.join(filepath,file)
	with open (inputfilepath) as f:
		contentofinput = f.read()
		print(contentofinput)
		print(type(contentofinput))
		#hex
		if contentofinput[0] == h or contentofinput[0]==H:
			print("it is hexadecimal")
			hexcode = re.findall('(?<=:).*$',contentofinput)
			print(hexcode)
			#hewcode is a list
			hexText = ''.join(str(i) for i in hexcode)
			#hexText is a str
			hex_split = hexText.split(" ")
			dictofhex = {
						'61':'a',
						'62':'b',
						'63':'c',
						'64':'d',
						'65':'e',
						'66':'f',
						'67':'g',
						'68':'h',
						'69':'i',
						'6a':'j',
						'6b':'k',
						'6c':'l',
						'6d':'m',
						'6e':'n',
						'6f':'o',
						'70':'p',
						'71':'q',
						'72':'r',
						'73':'s',
						'74':'t',
						'75':'u',
						'76':'v',
						'77':'w',
						'78':'x',
						'79':'y',
						'7a':'z',
						'41':'a',
						'42':'b',
						'43':'c',
						'44':'d',
						'45':'e',
						'46':'f',
						'47':'g',
						'48':'h',
						'49':'i',
						'4a':'j',
						'4b':'k',
						'4c':'l',
						'4d':'m',
						'4e':'n',
						'4f':'o',
						'50':'p',
						'51':'q',
						'52':'r',
						'53':'s',
						'54':'t',
						'55':'u',
						'56':'v',
						'57':'w',
						'58':'x',
						'59':'y',
						'5a':'z',
						'21':'!',
						'28':'(',
						'29':')',
						'2c':',',
						'2d':'-',
						'2e':'.',
						'3a':':',
						'3b':';',
						'3f':'?',
						'5f':'_',
						'7b':'{',
						'7d':'}',
						'20':' ',
						'30':'0',
						'31':'1',
						'32':'2',
						'33':'3',
						'34':'5',
						'35':'6',
						'36':'7',
						'37':'8',
						'38':'9',
						};
			for item in hex_split:
				print(dictofhex[item],end="")
				resultofhex = str(dictofhex[item])
				fp.write(resultofhex)
				fp.close


		#caeser
		elif contentofinput[0] ==c or contentofinput[0] == C:
			print("it is caesar")
			caesarcode = re.findall('(?<=:).*$',contentofinput)
			print(caesarcode)
			cipherText = ''.join(str(i) for i in caesarcode)
			print(cipherText)

			
			list1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
			list2 = ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c',' ']
			
			resultofcipher = str()
			for i in range(len(cipherText)):
				
					for j in range(0,len(list1)):
						if cipherText[i] == list2[j]:
							print(list1[j],end = '')
		
			fp.write(resultofcipher)
			fp.close



		#morse
		elif contentofinput[0] == m or contentofinput[0] == M:
			print("it is morse code")
			morsecode = re.findall('(?<=:).*$',contentofinput)
			print(morsecode)
			morseText = ''.join(str(i) for i in morsecode)
			code_split = morseText.split(" ")
			dictofmorse = {'.-':'a',
							'-...':'b',
							'-.-.':'c',
							'-..':'d',
							'.':"e",
							'..-.':'f',
							'--.':'g',
							'....':'h',
							'..':'i',
							'.---':'j',
							'-.-':'k',
							'.-..':'l',
							'--':'m',
							'-.':'n',
							'---':'o',
							'.--.':'p',
							'--.-':'q',
							'.-.':'r',
							'...':'s',
							'-':'t',
							'..-':'u',
							'...-':'v',
							'.--':'w',
							'-..-':'x',
							'-.--':'y',
							'--..':'z',
							'.-.-.-':'.',
							'--..--':',',
							'..--..':'?',
							'..--.':'!',
							'---...':':',
							'.-..-.':'"',
							'-.--.-':'()',
							'-....-':'-',
							'/':' ',
							'.----':'1',
							'..---':'2',
							'...--':'3',
							'....-':'4',
							'.....':'5',
							'-....':'6',
							'--...':'7',
							'---..':'8',
							'----.':'9',
							'-----':'0'
							};
			for item in code_split:
				print(dictofmorse[item],end="")
				resultofmorse = str(dictofmorse[item])
				fp.write(resultofmorse)
				fp.close
	            