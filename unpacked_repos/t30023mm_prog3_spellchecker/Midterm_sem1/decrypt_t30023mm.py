import os,sys 
inputfile=sys.argv[1]
path1=os.listdir(inputfile)
outputfile=sys.argv[2]



def decryption():
	for i in x.split(":"):
		if i in "Hex" or i[0] in 'h' or i[0] in 'H':
			hex()

		elif i in "Caesar Cipher(+3)" or i[0] in 'c' or i[0] in 'C':
			caesar()

		elif i in "Morse Code" or i[0] in 'm' or i[0] in 'M':
			morse()
	
	
					
def hex():
	str1=""
	text=False
	sum_=0
	for i in x.split(":"):
		if text==False:
			text=True
			continue
		for num in i.split():
			
			ctr = len(num)-1
		
			for digit in num:
			
				if digit in "1234567890":
					op = int(digit) * 16**ctr
					sum_+=op
					ctr-=1
				elif digit in " ":
					continue
				else:
					if digit in 'aA':
						op= 10 * 16**ctr 
						sum_+=op 
						ctr-=1
					elif digit in 'bB':
						op= 11 * 16**ctr 
						sum_+=op 
						ctr-=1
					elif digit in 'cC':
						op= 12 * 16**ctr 
						sum_+=op 
						ctr-=1
					elif digit in 'dD':
						op= 13 * 16**ctr 
						sum_+=op 
						ctr-=1
					elif digit in 'eE':
	
						op= 14 * 16**ctr 
						sum_+=op 
						ctr-=1

					elif digit in 'fF':
						op= 15 * 16**ctr 
						sum_+=op 
						ctr-=1
					else:
						break
			str1+=chr(sum_)
			sum_=0
		str1+=chr(sum_)
	str2=""
	for i in str1:
		if i.isupper()==True:
			str2+=i.lower()
		elif i.isalnum()==True:
			str2+=i
		elif i in " ":
			str2+=i
		else:
			continue
	print(str2)
	file2.write(str2)

def caesar():
	alphabet="xyzabcdefghijklmnopqrstuvw"
	str1=""
	text=False
	for i in x.split(":"):
		if text==False:
			text=True
			continue
		for word in i.split():
			for char in word:
				position=alphabet.index(char)
				str1+=alphabet[position-3]
			str1+=" "
	#print(str1)
	file2.write(str1) 



def morse():
	str1=""
	morsecode={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....',
	           'i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.',
	           'q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
	           'y':'-.--','z':'--..'}
	char=morsecode.items()
	text = False
	for i in x.split(":"):
		if text==False:
			text=True
			continue
		for num in i.split():
			
			if num in '/':
				str1+=" "
			for key,val in char:
				if val==num:
					str1+=key
	#print(str1)
	file2.write(str1)
			

for file in range(len(path1)):
	name_input=path1[file]
	a=os.path.join(inputfile,name_input)
	file1=open(a,"r")
	name=""
	for letter in name_input:
		if letter==".":
			break
		else:
			name+=letter
	name_output=name+"_t30023mm"
	b=os.path.join(outputfile,name_output)
	file2=open(b,"w")

	x=file1.read()
	decryption()
