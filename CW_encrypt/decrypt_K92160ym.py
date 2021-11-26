import argparse,os,re
parser=argparse.ArgumentParser(description="Determining which encryption method is used to encrypt the string and decrypte it!")
parser.add_argument("dir",nargs="+")
args = parser.parse_args()
filesStored=os.listdir(args.dir[0])

for i in range (0,len(filesStored)):
	name=filesStored[i].replace(".txt","")
	name_file=args.dir[0]+"/"+filesStored[i]
	
	result_file=open(name_file,"r")
	inputText=result_file.read()
	pargr=inputText.split(":")
	text=pargr[1]
	print(text)
	isHex=0	
	num="1234567890"
	j=0
	j in range(len(num))

	if "."and"-" in text :
	
		text=text.replace("/","")
		
		print("  we will use Morse algorithm to decrypte the code:  ")
		
		morse_code = { 'A':'.-', 'B':'-...',
						'C':'-.-.', 'D':'-..', 'E':'.',
						'F':'..-.', 'G':'--.', 'H':'....',
						'I':'..', 'J':'.---', 'K':'-.-',
						'L':'.-..', 'M':'--', 'N':'-.',
						'O':'---', 'P':'.--.', 'Q':'--.-',
						'R':'.-.', 'S':'...', 'T':'-',
						'U':'..-', 'V':'...-', 'W':'.--',
						'X':'-..-', 'Y':'-.--', 'Z':'--..',
						'1':'.----', '2':'..---', '3':'...--',
						'4':'....-', '5':'.....', '6':'-....',
						'7':'--...', '8':'---..', '9':'----.',
						'0':'-----', ', ':'--..--', '.':'.-.-.-',
						'?':'..--..', '/':'-..-.', '-':'-....-',
						'(':'-.--.', ')':'-.--.-'}

		def decrypt(msg):

			decryptedText = ''
			citext = ''
			for letter in msg:

				if (letter != ' '):	
					i = 0

					citext += letter

				else:
				
					i += 1
					if i == 2 :
						decryptedText += ' '
					else:
						decryptedText += list(morse_code.keys())[list(morse_code
						.values()).index(citext)]
						citext = ''
						

			return decryptedText

		
		result = decrypt(text)
		string=result.lower()
		print(string)
		
		appearfile=str(args.dir[1])+"/"+ name + "_K92160ym.txt"
		write_f=open(appearfile,"w")
		output=string
		write_f.write(output)



	else:
		for elm in text:
			if elm in num :
				isHex=1

		if isHex == 1:

			print("  we will use Hexadecimal algorithm to decrypte the code: ")
			text=text.replace(" ","")
			bytes_object = bytes.fromhex(text)
			string = bytes_object.decode("ASCII")
			print(string)

			appearfile=str(args.dir[1])+"/"+ name + "_K92160ym.txt"
			write_f=open(appearfile,"w")
			output=string
			write_f.write(output) 


		else :
			print("  we will use caesar algorithm to decrypte the text:")
			
					
				
				
			def csr():
				alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
				text1=""
				index1=0
				for z in text:
					if z==" ":
						text1+=" "
					elif z!=" ":
						index1 = alph.index(z)
						index1=index1-3
						text1+=alph[index1]
				
				return text1

			
			string=csr()
			print(string)
			appearfile=str(args.dir[1])+"/"+ name + "_K92160ym.txt"
			write_f=open(appearfile,"w")
			output=string
			write_f.write(output)


	







	