import argparse
import os
import re

Parser=argparse.ArgumentParser()
Parser.add_argument("input",nargs="+")
args=Parser.parse_args()
# args.input[0]
x=os.listdir(args.input[0])

# y=args.input[0]+"/"+x



for a in range(0,len(x)):
	y=args.input[0]+"/"+x[a]

	text=open(y,'r')
	ciphertext=text.read()

	plaintext=""

	for b in range(0,len(ciphertext)):

		if ciphertext[b]==":":
			if ciphertext[b-1]==")":
				
				ciphertextPosition = 18
				ciphertext=re.sub(' ','#', ciphertext)

				while (ciphertextPosition < len(ciphertext)):

					ciphertextChar=ciphertext[ciphertextPosition]
					ASCIIValue=ord(ciphertextChar)
					ASCIIValue=ord(ciphertextChar) - 3
					plaintext=plaintext+chr(ASCIIValue)
					ciphertextPosition=ciphertextPosition + 1
							


				# print(plaintext)

			elif ciphertext[b-1]=="x":

				ciphertext=ciphertext[4:]
				ciphertext=bytes.fromhex(ciphertext)
				plaintext=ciphertext.decode("ASCII")
			# print(plaintext)
			# break
			
			else:
				ciphertext=ciphertext[11:]
				code=""
				k=[]
				morsecode = {'..-.': 'f', '-..-': 'x',
                 '.--.': 'p', '-': 't', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'v', '-.-.': 'c', '.': 'e', '.---': 'j',
                 '---': 'o', '-.-': 'k', '----.': '9', '..': 'i',
                 '.-..': 'l', '.....': '5', '...--': '3', '-.--': 'y',
                 '-....': '6', '.--': 'w', '....': 'h', '-.': 'n', '.-.': 'r',
                 '-...': 'b', '---..': '8', '--..': 'z', '-..': 'd', '--.-': 'q',
                 '--.': 'g', '--': 'm', '..-': 'u', '.-': 'a', '...': 's', '.----': '1', '/': " ",
                 '._._._': '.', '__..__': ',', '..__..': "?", '_._._.': ";", '___...': ":", '_...._': "-", '_.._.': "/",
                 '.____.': "'", '._.._.': '"', '_.__._': ")", '_.__.': "(", '-.-.--': "!"}
								
				for i in ciphertext:
					
					if i != ' ':
						code=code+i
					
					 
					elif i == ' ':
						plaintext+=morsecode[code]
						code = ''
						# plaintext=k.append(code)
						print(plaintext)
						# plaintext=plaintext.split()
						# k=[]
						# plaintext=k.append(plaintext)
						# print(plaintext)
						

					# elif i == '/':
					# 	plaintext=morsecode[code]

				
						# plaintext = ''.join(plaintext)
						# plaintext=str(plaintext, end='')
						# print(plaintext)
						# code = ''


			break

	
#     ciphertext:plaintext
# 	for x in ciphertext:
# 		code=""
# 		if x==" ":
# 			plaintext=plaintext+morsecode[code]
# 			code=""
# 		else:
# 			code=code+x



	r=args.input[1]+"/"+x[a]
	result=plaintext.lower()
	o=r.replace(".", "_g78196wl.")
	f=open(o,'w')
	f.write(result)





