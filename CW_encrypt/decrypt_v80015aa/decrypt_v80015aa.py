import sys
import os

morseDictionary =  {
    '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ', '.----': '1',  '..---': '2',  '...--': '3', '....-': '4',  '.....': '5',  '-....': '6', '--...': '7',  '---..': '8',  '----.': '9'
}
ceaserDictionary = { 
'x' : 'a', 'y' : 'b', 'z' : 'c', 'a' : 'd', 'b' : 'e', 'c' : 'f', 'd' : 'g', 'e' : 'h', 'f' : 'i', 'g' : 'j', 'h' : 'k', 'i' : 'l', 'j' : 'm', 'k' : 'n', 'l' : 'o', 'm' : 'p', 'n' : 'q', 'o' : 'r', 'p' : 's', 'q' : 't', 'r' : 'u', 's' : 'v', 't' : 'w', 'u' : 'x', 'v' : 'y', 'w' : 'z'
}
ceaser = "abcdefghijklmnopqrstuvwxyz"

n = 0

currentfile = os.getcwd()

testfiles = os.listdir(sys.argv[1])

resultsfolder = sys.argv[2]+"/"
#os.chdir(sys.argv[1])
for file in testfiles:
	os.chdir(sys.argv[1])
	filename = file[:-4] + "_v80015aa.txt"
	finalWord = ""
	inputfile = open(file, "r")
	x = inputfile.read()
	begin = x.find(":")
	i = x[begin+1:] #Use + 1 so the ":" is not included
	if x[0:3].lower() == "mor":
		w = i.split()
		for word in w:
			finalWord = finalWord + morseDictionary[word]

	elif x[0:3].lower() == "hex":
		finalWord = bytes.fromhex(i).decode("ascii").lower()
		
	elif x[0:3].lower() == "cae":
		p = i.lower()

		for letter in p:
			if letter == " ":
				finalWord = finalWord + " "
			else:
				n = ceaser.find(letter)
				finalWord += ceaser[n-3]

		finalWord = finalWord[:-1]

		#z = p.replace("a", "x").replace("b", "y").replace("c", "z").replace("d", "a").replace("e", "b").replace("f", "c").replace("g", "d").replace("h", "e").replace("i", "f").replace("j", "g").replace("k", "h").replace("l", "i").replace("m", "j").replace('n', 'k').replace("o", "l").replace('p', 'm').replace("q", "n").replace("r", "o").replace("s", "p").replace("t", "q").replace("u", "r").replace('v', 's').replace("w", "t").replace('x', 'u').replace("y", "v").replace('z', 'w')
		#for letter in z:
			#if letter == " ":
				#finalWord = finalWord + " "
			#else:
				#finalWord = finalWord + ceaserDictionary[letter]
	#currentfile = os.getcwd()
	os.chdir(currentfile)
	outputfile = open(resultsfolder + filename, "w")
	outputfile.write (finalWord)
	outputfile.close()


