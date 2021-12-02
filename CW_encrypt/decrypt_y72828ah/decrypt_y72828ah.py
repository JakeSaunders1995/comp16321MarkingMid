import os
import sys
inputf = sys.argv[1]
outputf = sys.argv[2]
def decryptmorse(text):
	morsedict = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e",
	"..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",
	".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r",
	"...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y",
	"--..":"z",".....":" ","--..--":",",".-.-.-":".","..--..":"?","-.-.-.":";",
	"---...":":","-..-.":"/","-....-":"-",".----.":"'",".-..-.":"\"","-.--.":"(",
	"-.--.-":")","-.-.--":"!"}
	plainl = []
	wordlist = text.split(" / ")
	for i in wordlist:
		charlist = i.split(" ")
		for i in charlist:
			plainl.append(morsedict[i])
		plainl.append(" ")
	plaint = ''.join([str(item) for item in plainl])
	return plaint
			

def decrypthex(text):
	plaint = bytes.fromhex(text).decode('utf-8')
	plaint = plaint.lower()
	return plaint
def decryptcaesar(text):
	lower = text.lower()
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	plainl = []

	for letter in lower:
		if letter in alphabet:
			index = alphabet.index(letter)
			indexf = (index-3)
			if indexf <0:
				indexf += 26
			plainl.append(alphabet[indexf])
		else:
			plainl.append(letter)
	plaint = ''.join([str(item) for item in plainl])
	return plaint




def whichdecrypt(encryption,ciphertext):
	plaintext = False
	if encryption == "Caesar Cipher(+3)":
		plaintext = decryptcaesar(ciphertext)
	elif encryption == "Hex":
		plaintext = decrypthex(ciphertext)
	elif encryption == "Morse Code":
		plaintext = decryptmorse(ciphertext)
	else:
		print("No encrpytion method")
	return plaintext

for x in os.listdir(inputf):
	f = os.path.join(inputf,x)
	text = open(f)
	line = text.readline()
	filename = os.path.basename(x)
	split = line.split(":")
	encryption = split[0]
	ciphertext = split[1]
	plaintext = whichdecrypt(encryption,ciphertext)
	filename = filename.replace(".txt","")
	outputname = outputf + "/" + filename+"_y72828ah.txt"
	outputfile = open(outputname, "w")
	outputfile.write(plaintext)
	outputfile.close()

