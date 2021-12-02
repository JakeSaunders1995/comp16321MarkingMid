import sys, os
import string 

inputoutput = sys.argv


#input/output should be the whole dir including root 
inpath = sys.argv[1]
outpath = sys.argv[2]

os.chdir(inpath)

res = []
alph = 'abcdefghijklmnopqrstuvwxyz'
morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')'}


for file in os.listdir():
	if file.endswith(".txt"):
		file_path = f"{inpath}/{file}"
		with open(file_path, 'r') as f:
			data = f.read().split(":")
			algo = data[0]
			cipher = data[1]

			if algo.lower() == 'hex':
				split = cipher.split()
				temp = ''
				for i in split:
					temp += bytearray.fromhex(f'{i}').decode()
				res.append(temp)
			

			#
			elif algo[0:6] == 'Caesar':
				temp = ''
				for i in cipher:
					if i != " ":
						temp += alph[alph.find(i) - 3 ]
					else:
						temp += " "
				
				#jesus christ why did they make strings immutable, wasted so much time on this.
				res.append(temp.replace('w', ''))
			else:
				
				split = cipher.split()

				temp = ''
				for i in split:
					print(i)
					if i in morse.keys():
						temp += morse.get(i)
					elif i == "/": 
						temp += ' '
				res.append(temp.lower())


		os.chdir(outpath)
		for i in range(len(res)):
			f = open(f'{file} g28708at.txt', "w")
			f.write(res[i])



	  
