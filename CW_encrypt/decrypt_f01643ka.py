import os.path
import sys

morse = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e',
         '..-.':'f','--.':'g','....':'h','..':'i','.---':'j',
         '-.-':'k','.-..':'l','--':'m','-.':'n','---':'o',
         '.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t',
         '..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y',
         '--..':'z','.----':'1','..---':'2','...--':'3','....-':'4',
         '.....':'5','-....':'6','--...':'7','---..':'8','----.':'9',
         '----':'0','--..--':',', '.-.-.-':'.','..--..':'?',
         '-..-.':'/','-....-':'-','-.--.':'(','-.--.-':')'}
caesar = "xyzabcdefghijklmnopqrstuvwxyz"
inputfolder = sys.argv[1]
output = sys.argv[2]
for filename in os.listdir(inputfolder):
	fpath = inputfolder + "/" + filename
	filetxt= open(fpath, "r")
	file = filetxt.read()
	i = 0
	if file[i] == "H":
		text = file[4:]
		senb = bytes.fromhex(text)
		sen = senb.decode("ascii")
	elif file[i] == "C":
		sen =""
		for char in file[18:]:
			if char == " ":
				sen+= " "
			elif char in caesar[3:]:
				p = caesar.index(char)
				p-= 3
				sen += caesar[p]
			elif char == "x":
				sen+= "u"
	elif file[i] == "M":
		sen = ""
		file = file[11:]
		words = file.split(' /')
		for x in words:
			letter = x.split(' ')
			asciil = ""
			w = ""
			i = -1
			for y in letter:
				i+= 1
				asciil+= morse.get(letter[i],' ')
			w += asciil
			sen += w 
	outfile = output + "/" + filename[0:10] +"_f01643ka" + ".txt"
	tempout = open(outfile, "w")
	tempout.write(sen)
	tempout.close()



