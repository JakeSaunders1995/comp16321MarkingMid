import sys
import os

input_Folder = sys.argv[1]
output_Folder = sys.argv[2]
fileList = os.listdir(input_Folder)
for filename in fileList:
	encrypted = open(input_Folder + "/" + filename)
	encryptiontam = encrypted.read()
	encrypted.close()
	def decryption():
		decryption.decryptedMess = ""
		if encryptiontam[0] == "H":
			colonPos = encryptiontam.find(":")
			encryptedMess = encryptiontam[colonPos + 1 : len(encryptiontam)]
			decryption.decryptedMess = bytes.fromhex(encryptedMess)
			decryption.decryptedMess = decryption.decryptedMess.decode("ascii")
			decryption.decryptedMess = decryption.decryptedMess.lower()
		elif encryptiontam[0] == "C":
			colonPos = encryptiontam.find(":")
			encryptedMess = encryptiontam[colonPos + 1 : len(encryptiontam)]
			alphabet = "abcdefghijklmnopqrstuvwxyz"
			for i in range(len(encryptedMess) - 1):
				if encryptedMess[i] != " ":
					pos = alphabet.find(encryptedMess[i])
					plainChar = alphabet[pos - 3]
					decryption.decryptedMess += plainChar
				else:
					decryption.decryptedMess += encryptedMess[i]
		elif encryptiontam[0] == "M":
			colonPos = encryptiontam.find(":")
			encryptedMess = encryptiontam[colonPos + 1 : len(encryptiontam)]
			morseKey = {
			".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
			"....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n",
			"---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
			"..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",
			"-----": "0", ".----": "1", "..---":"2", "...--": "3", "....-": "4",
			".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
			".-.-.-": ".", "---...": ":", "--..--":",", "-.-.-.": ";", "..--..": "?",
			"-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
			"..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
			".-...": "&", ".--.-.": "@", ".-.-.": "+", "/": " "
       		}
			encryptedMess += "  "
			i = 0
			newList = []
			emptyString = ""
			while True:
				if i == len(encryptedMess) - 1:
					break
				elif encryptedMess[i] != " ":
					emptyString += encryptedMess[i]
				elif encryptedMess[i] == " ":
					newList.append(emptyString)
					emptyString = ""
				i += 1			
			for key in newList:
				decryption.decryptedMess += morseKey.get(key)
	decryption()
	decrypted_File = open(output_Folder + "/" + filename[0:len(filename) - 4] + "_s93700yl.txt", "w")
	decrypted_File.write(decryption.decryptedMess)
	decrypted_File.close()




