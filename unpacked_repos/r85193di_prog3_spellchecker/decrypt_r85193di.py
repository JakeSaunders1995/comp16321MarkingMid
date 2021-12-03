
import argparse, os


parser = argparse.ArgumentParser()
parser.add_argument('dirctry')
parser.add_argument('decodedfile')
args = parser.parse_args()

strfile = os.listdir(args.dirctry)
outputfile = os.listdir(args.decodedfile)
q=0
while q<len(strfile):
	
	file = args.dirctry+"/"+strfile[q]
	encryptedfile = open(file, "r")
  #initialising variables
	encryptionused=0
	testword =""
	i=0
	x=0
	encryptedtext=""

	while True:#checking to see what type of encryption has been used 
	    w = encryptedfile.read(1)#reading each charactyer in a file
	    if testword=="Hex":
	    	encryptionused=1
	    if testword=="Caesar Cipher(+3)":
	    	encryptionused=2
	    if testword=="Morse Code":
	    	encryptionused=3
	    if not w:
	      break
	    testword = testword + w# adding each character into a variable list/array

	encryptedfile.close()
	found = True
	#identifying where colon is
	while i<len(testword) and found == True:
		if testword[i] == ":":
			found = False
			x = i + 1#first letter to decode must be one character after location of colon
			
		i+=1   


	while x<len(testword):# adding all characters to be decoded into an fresh variable list/array
			encryptedtext = encryptedtext + testword[x]
			x+=1

	plaintext = ""
	ascval=1
	if encryptionused == 1:#if hex has been used 
		ctposition = 0
		i=0
		while ctposition < (len(encryptedtext)-2):#bcs hex are stored in pairs 
			i+=1
			
			hexbyte1 = encryptedtext[ctposition]#since pairs; taking two at a time and converting them into hex
			hexbyte2 = encryptedtext[ctposition+1]
			if hexbyte1 == " " or hexbyte2 == " ":#if one of the characters is a space; move up 
				ctposition += 1
				i=0
			else:
				ct1 = int(hexbyte1,base=16)#converting from string to hex
				ct2 = int(hexbyte2,base=16)
				ctchar = chr((ct1 * 16) + (ct2))# converting fro hex to decimal
				plaintext = plaintext + ctchar.lower()#making sure its lowercase
				ctposition +=1
				i+=1
				
		
	if encryptionused == 2:#if ceaser encryption has been used
		ctposition = 0

		while ctposition < len(encryptedtext):#checking each character
			ctchar = encryptedtext[ctposition]
			if ctchar == " ":# if its a space move to the next character and print the space
				plaintext = plaintext + " "
				ctposition += 1
			else:
				ascval = ord(ctchar)# converting non-space character into its ASCII/unicode value
				ascval = ascval - 3#subtracting 3 from its ASCII/unicode value
				plaintext = plaintext + chr(ascval).lower()#reconverting it into a character then making it lowercase
				ctposition +=1


	#morsecode dictionary
	morseCodeDIctionary=["'A':'.-'","'B':'-...'","'C':'-.-.'","'D':'-..'","'E':'.'","'F':'..-.'","'G':'--.'","'H':'....'","'I':'..'","'J':'.---'","'K':'-.-'","'L':'.-..'","'M':'--'","'N':'-.'","'O':'---'","'P':'.--.'","'Q':'--.-'","'R':'.-.'","'S':'...'","'T':'-'","'U':'..-'","'V':'...-'","'W':'.--'","'X':'-..-'","'Y':'-.--'","'Z':'--..'","'1':'.----'","'2':'..---'","'3':'...--'","'4':'....-'","'5':'.....'","'6':'-....'","'7':'--...'","'8':'---..'","'9':'----.'","'0':'-----'","', ':'--..--'","'.':'.-.-.-'","'?':'..--..'","'/':'-..-.'","'-':'-....-'","'(':'-.--.'","')':'-.--.-'"]

	if encryptionused==3:#if morsecode has been used
		i=0
		m=0
		while i < (len(encryptedtext)-1):#check every character in encrypted text            
			i+=1
			if encryptedtext[i] == " ":#if space has been found anything from m to current location must be a character to be decoded
				letter = encryptedtext[m:i]
				
				m = i + 1#identifying where next character starts
				z = 0

				if letter == "/":# if letter is a space
					plaintext = plaintext + " "# add space to decryption

				while z < len(morseCodeDIctionary):#checking each charcter in morsecode dictionary
					caseletter=morseCodeDIctionary[z]
					if caseletter[5:(len(caseletter)-1)] == letter:# each morsecode character is from the 5th character to the length of each character
						plaintext = plaintext + caseletter[1].lower()#locating character and converting to lowercase
						break
					else:
						z+=1
			
		letter=encryptedtext[i]
		while z < len(morseCodeDIctionary):# checking last character in encrypted text to convert to plaintext
			caseletter=morseCodeDIctionary[z]
			if caseletter[5:(len(caseletter)-1)] == letter:
				plaintext = plaintext + caseletter[1].lower()
				break
			else:
				z+=1

	decodedfile = strfile[q]
	decoded = decodedfile[0:len(decodedfile)-4]+"_r85193di.txt"
	print(plaintext)
	outputfile = open(decoded, "w")
	outputfile.write(plaintext)
	outputfile.close()

	q+=1