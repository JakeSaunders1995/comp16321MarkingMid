def Caesar(NoShifts, caeCiph):
	caePlain = ""
	Shifts = 0
	for y in range(27):
		if str(y) in NoShifts:
			Shifts = int(y)
			break
	for x in caeCiph:
		if(x == " "):
			caePlain = caePlain + " "
		else:
			if((ord(x) - Shifts) < 97):
				caePlain = caePlain + chr(122-(abs(Shifts- ord(x)+97-1)))
			else:
				caePlain = caePlain + chr(ord(x)-Shifts)
	return caePlain

def Hex(hexCiph):
	hexPlain = bytes.fromhex(hexCiph).decode("ascii")
	return hexPlain



def Morse(morseCiph):

	MorseCodeTranslator= {'....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ', '-.-.--': '!', '---...' : ':', '-.-.-.': ';', '-....-': '-', '-.--.': '(', '-.--.-': ')', '.-..-.': '"', '.----.':"'", '.-.-.-.-.-.-.-.-.-' : '...'}
	somet = morseCiph.split(' ')
	morsePlain = ''
	for x in somet:
		morsePlain = morsePlain + MorseCodeTranslator[x]
	return morsePlain
	

import sys, os
for file in os.listdir(sys.argv[1]):
	with open(os.path.join(sys.argv[1], file)) as cipherFile:
		cipherText = cipherFile.readlines()

	cipherID = cipherText[0].split(":")
	plainText = ''
	if("Morse Code" in cipherID[0]):
		plainText = Morse(cipherID[1])
	elif("Hex" in cipherID[0]):
		plainText = Hex(cipherID[1])
	else:
		plainText = Caesar(cipherID[0], cipherID[1])

	plainText = plainText.lower()

	for outputFile in os.listdir(sys.argv[2]):
		correspondFile = os.path.splitext(file)[0] + "_e40896us"
		if(correspondFile == os.path.splitext(outputFile)[0]):
			with open(os.path.join(sys.argv[2], outputFile), 'w') as plainFile:
				plainFile.write(plainText)

