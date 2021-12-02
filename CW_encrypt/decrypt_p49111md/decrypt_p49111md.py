import os
import sys
path=sys.argv[1]
path2=sys.argv[2]

dirs=os.listdir(path)
for x in dirs:
	file=open(path+'/'+x,'r')
	text=file.read()
	file.close()

	morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]
	alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	split=text.partition(':')

	if split[0]=='Hex':
		cipher=split[2]
		temp=bytearray.fromhex(cipher)
		plaintext=temp.decode()
		print(plaintext)
	elif split[0]=='Morse Code':
		plaintext=''
		temp=split[2]
		cipher=temp.split('/')
		for i in range(len(cipher)):
			temp=cipher[i]
			char=temp.split(' ')
			for e in range(len(char)):
				for a in range(len(morse)):
					if char[e]==morse[a]:
						plaintext+=alphabet[a]
			plaintext+=' '
		print(plaintext)
	else:
		plaintext = ''
		ciphertext = split[2]
		ciphertextPosition =0
		while (ciphertextPosition< len(ciphertext)):
		    ciphertextChar = ciphertext[ciphertextPosition]
		    if ciphertextChar==' ':
		    	plaintext+=' '
		    	ciphertextPosition = ciphertextPosition +1
		    elif ciphertextChar=='a':
		    	plaintext+='x'
		    	ciphertextPosition = ciphertextPosition +1
		    elif ciphertextChar=='b':
		    	plaintext+='y'
		    	ciphertextPosition = ciphertextPosition +1
		    elif ciphertextChar=='c':
		    	plaintext+='z'
		    	ciphertextPosition = ciphertextPosition +1
		    elif ciphertextChar=='0':
		    	plaintext+='7'
		    	ciphertextPosition = ciphertextPosition +1
		    elif ciphertextChar=='1':
		    	plaintext+='8'
		    	ciphertextPosition = ciphertextPosition +1
		    elif ciphertextChar=='2':
		    	plaintext+='9'
		    	ciphertextPosition = ciphertextPosition +1
		    else:
			    ASCIIValue = ord(ciphertextChar)
			    ASCIIValue = ASCIIValue - 3
			    plaintext = plaintext +chr(ASCIIValue)
			    ciphertextPosition = ciphertextPosition +1
		print (plaintext)
	
	l=x[:-4]
	myfile=open(path2+'/'+l+'_p49111md.txt','w')
	myfile.write(plaintext)

