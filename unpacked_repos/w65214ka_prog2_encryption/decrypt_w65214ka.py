import os
import sys
import codecs
morse = {
    '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
}
base= os.getcwd()
chars = 'abcdefghijklmnopqrstuvwxyz'

folder  = os.listdir(sys.argv[1])

for file in folder:
	os.chdir(sys.argv[1])
	with open(file, 'r') as f:
		contents = f.read()

	x=0
	while contents[x] != ":":
		x+= 1
	code = contents [x+1:]
	decrypted = ""

	if contents[0] == 'm' or contents[0] == 'M':
		code = code.split()
		for i in code:
			decrypted += morse[i]

	elif contents[0] == 'h' or contents[0] == 'H':
		code = code.split()
		for i in code:
			decrypted += (codecs.decode(i,"hex")).decode('UTF-8') 

	elif contents[0] == 'c' or contents[0] =='C':
		code.lower()
		for i in code:
			if i != " ":
				x = chars.find(i)
				decrypted += chars[x-3]
			else:
				decrypted += i
		decrypted=decrypted[0:-1]
	new_file = sys.argv[2] + "/" + file[:-4] +"_w65214ka.txt"
	os.chdir(base)
	text_file = open(new_file, 'w')
	text_file.write(decrypted)
	text_file.close()
