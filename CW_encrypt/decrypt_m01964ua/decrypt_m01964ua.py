import sys, os  

insertFolder = sys.argv[1] 
prep = os.listdir(insertFolder) 
os.mkdir(sys.argv[2]) 
# to iterate through all files
for q in prep: 
	e = insertFolder + "/" + q 
	with open(e,'r') as insert1: 
		insert = insert1.read() 
		ehco = "" 
		text = [] 
		result = "" 
		hCode = [] 
		#Solving hexadecimal code
		if "Hex:" in insert: 
			w = 0; v = 4; 
			while v < len(insert): 
				if v == len(insert) - 1: 
					hCode.append(insert[v]) 
					v = v + 1 
					echo = hCode[0] + hCode[1] 
					key = int(echo, 16) 
					text.append(chr(key))
					hCode = [] 
				elif insert[v] == " ": 
					echo = hCode[0] + hCode[1] 
					key = int(echo, 16) 
					text.append(chr(key))
					hCode = [] 
					v = v + 1 
				else: 
					hCode.append(insert[v])
					v = v + 1
			while w < len(text): 
				result += text[w] 
				w = w + 1 
		#Solving Caesar code		
		elif "Caesar Cipher(+3):" in insert: 
			cCode = "" 
			#letters = "xyzabcdefghijklmnopqrstuvwxyzabc" 
			codePoint = 18 
			while (codePoint < len(insert)): 
				codePointChar = insert[codePoint] 
				if codePointChar == " ":
					result = result + " " 
					codePoint = codePoint + 1 
				else: 
					ASCIIValue = ord(codePointChar) - 3
					result += chr(ASCIIValue)
					codePoint = codePoint + 1	
		#Solving Morse code				
		elif "Morse Code:" in insert: 
			morseText = ""  
			word = []
			#using dictionary to create the conversions of morse code:
			theCode = {'.-':'a','-...':'b', '-.-.':'c',
					'-..':'d', '.':'e', '..-.':'f',
					'--.':'g', '....':'h', '..':'i',
					'.---':'j','-.-':'k', '.-..':'l',
					'--':'m', '-.':'n', '---':'o',
					'.--.':'p', '--.-':'q', '.-.':'r',
					'...':'s','-':'t','..-':'u',
					'...-':'v', '.--':'w', '-..-':'x',
					'-.--':'y', '--..':'z', '.....':' ',
					'-----':'0','.----':'1','..---':'2',
					'...--':'3','....-':'4','.....':'5',
					'-....':'6','--...':'7','---..':'8',
					'----.':'9','.-.-.-':'.','..--..':'?', 
					'-.-.--':'!','--..--':',','---...':':',
					'-.-.-.':';','-....-':'-','..--.-':'_',
					'-.--.':'(','-.--.-':')','.----.':"'",
					'.-..-.':'"'}	
			for word in insert: 
				if word in theCode: 
					morseText = morseText + theCode[word] 
				elif word == '/': 
					morseText += " " 
			result = morseText	
	#creating output		
	fix = q.replace('.txt','')			 		
	output = sys.argv[2] + "/" + fix + "_m01964ua" + ".txt" 
	final = open(output, 'w')
	final.write(result)							




