#enc= "Morse Code:.... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -  "
import sys,os
from pathlib import Path
import ntpath

file1=sys.argv[1]
file2=sys.argv[2]

for in_entry in os.scandir(file1):
	f1=open(in_entry.path, 'r')
	enc=f1.readline().strip()
	f1.close() 
	f2=Path(in_entry).stem + "_e37076ka.txt"
	f2= os.path.join(file2, f2)
	f2out=open(f2, 'w+')
	#f2out.write(str(doc))
	#f2out.close()
	if enc[0]== 'C':
		plaintext=""
		cipherTextPosition=18
		while (cipherTextPosition)<(len(enc)):
			if(enc[cipherTextPosition] == " "):
				plaintext= plaintext+ " "
				cipherTextPosition=cipherTextPosition+1
			else:
				ciphertextChar=enc[cipherTextPosition]
				ASCIIValue=ord(ciphertextChar)
				ASCIIValue=ASCIIValue-3
				plaintext=plaintext+chr(ASCIIValue)
				cipherTextPosition=cipherTextPosition+1
		plaintext2=plaintext.lower()
		#print(plaintext2)
		f2out.write(str(plaintext2))

	if enc[0]== 'M':
		dic= {'a' : '.-',
		'b' : '-...',
		'c' : '-.-.',
		'd' : '-..',
		'e' : '.',
		'f' : '..-.',
		'g' : '--.',
		'h' : '....',
		'i' : '..',
		'j' : '.---',
		'k' : '-.-',
		'l' : '.-..',
		'm' : '--',
		'n' : '-.',
		'o' : '---',
		'p' : '.--.',
		'q' : '--.-',
		'r' : '.-.',
		's' : '...',
		't' : '-',
		'u' : '..-',
		'v' : '...-',
		'w' : '.--',
		'x' : '-..-',
		'y' : '-.--',
		'z' : '--..',
		' ' : '/',
		'1' : '.----',
		'2' : '..---',
		'3' : '...--',
		'4' : '....-',
		'5' : '.....',
		'6' : '-....',
		'7' : '--...',
		'8' : '---..',
		'9' : '----.',
		'0' : '-----'}

		plaintext3=""
		ci=enc[11:]
		dic_decrypt= { x:y for y, x in dic.items()}
		enc=ci.split()
		for z in enc:
			plaintext4= dic_decrypt.get(z)
			plaintext3= str(plaintext3)+ str(plaintext4)
		#print(plaintext3)
		f2out.write(str(plaintext3))

	if enc[0]== 'H':
		hextext=enc[4:]
		dec=bytes.fromhex(hextext)
		dec=dec.decode("ascii")
		smalleter= dec.lower()
		#print(smalleter)
		f2out.write(str(smalleter))
	f2out.close()

	'''if enc.startswith('C'):
		doc=cipherDecode(enc)
	elif enc.startswith('M'):
		doc=moreCode(enc)
	elif enc.startswith('H'):
		doc=hex(enc)'''

'''f2=Path(in_entry).stem + "_e37076ka.txt"
f2= os.path.join(file2, f2)
f2out=open(f2, 'w+')
f2out.write(str(doc))
f2out.close()'''
