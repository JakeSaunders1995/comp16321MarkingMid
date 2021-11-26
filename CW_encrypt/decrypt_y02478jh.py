import re, sys, os

morseCodeDic = {
		".-": "a", "-...": "b", "-.-.": "c",
		"-..": "d", ".": "e", "..-.": "f",
		"--.": "g", "....": "h", "..": "i",
		".---": "j", "-.-": "k", ".-..": "l",
		"--": "m", "-.": "n", "---": "o",
		".--.": "p", "--.-": "q", ".-.": "r",
		"...": "s", "-": "t", "..-": "u",
		"...-": "v", ".--": "w", "-..-": "x",
		"-.--": "y", "--..": "z", ".----": "1",
		"..---": "2", "...--": "3", "....-": "4",
		".....": "5", "-....": "6", "--...": "7",
		"---..": "8", "----.": "9", "-----": "0",  
		"/": " ", "..--..": "?", "-.-.-.": ";", "---...": ":", "-....-": "–",
		".-.-.-": ".", "-..-.": "/", ".----.": "'", ".-..-.": "\"", 
		"..--.-": "_", "-.--.": "(", "-.--.-": ")", "-.-.--": "!", "--..--": ","
}

contentInDir = []
for element in os.listdir(sys.argv[1]):
	contentInDir.append(os.path.join(sys.argv[1],element))
files = list(filter(os.path.isfile, contentInDir))
for eachFile in files:
	file = open(eachFile,"r")
	decryption = ""
	sentence = re.split(":", file.read())
	codeList = re.split(" ", sentence[1])
	file.close()

	for code in codeList:
		if (sentence[0] == "Morse Code"): 
			decryption += morseCodeDic[code]
		elif (sentence[0] == "Caesar Cipher(+3)"):
			for position in range(0, len(code)):
				if (code[position] == "a"):
						decryption += "c"
				elif (code[position] == "b"):
						decryption += "y"
				elif (code[position] == "c"):
						decryption += "z"
				else:
					decryption += chr(ord(code[position])-3)
			decryption += chr(32)
		elif (sentence[0] == "Hex"):
			decryption += bytearray.fromhex(code).decode()
		else:
			decryption = "please input the file in the right format, like (algorithm):(ciphertext)."
	
	output_file = open(os.path.join(sys.argv[2], eachFile[0 -(len(eachFile) - len(sys.argv[1]) - 1):-4] + "_y02478jh.txt"), "w")
	output_file.write(decryption.lower())
	output_file.close()












