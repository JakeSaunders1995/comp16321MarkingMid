
import sys
import os
import string

class Decrypt:
	
	def morse(self):
		morsealpha = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
		morsearr = morsealpha.split(" ")
		morsedic = {}
		alphabet = string.ascii_lowercase
		for x in range(len(morsearr)):
			morsedic[morsearr[x]] = alphabet[x]
		for wrd in self.st.split('/'):
			for let in wrd.split(" "):
				if let != '':
					self.strout += morsedic[let]
			self.strout += " "
		return self.strout

	def caes(self):
		cheat = {'a':'x','b':'y','c':'z'}
		self.st = self.st.lower()
		for char in self.st:
			if char == " ":
				self.strout+=" "
			else:
				if ord('a') <= ord(char) < ord('d'):
					self.strout += cheat[char]
				else:
					if ord('a') <= ord(char)-3 <= ord('z'):
						self.strout += chr(ord(char)-3)
		return self.strout

	def hex(self):
		newArr = self.st.split(" ")
		for idx in range(len(newArr)):
			rev = newArr[idx][::-1]
			rev += 'x0'
			self.strout += chr(int(rev[::-1],16))
		return self.strout.lower()

	def __new__(self,inp):
		self.encoding,self.st = inp.split(":")
		self.strout = ''
		if self.encoding == "Morse Code":
			return self.morse(self)
		elif self.encoding == 'Caesar Cipher(+3)':
			return self.caes(self)
		elif self.encoding == 'Hex':
			return (self.hex(self))
		else:
			return "unrecognized encoding"


owd = os.getcwd()
try :
	os.chdir(sys.argv[2])
except:
	os.mkdir(sys.argv[2])
	os.chdir(sys.argv[2])
outputfolderpath = os.getcwd()

try:
	os.chdir(sys.argv[1])
except:
	os.chdir(owd+"/"+sys.argv[1])
inputfolderpath = os.getcwd()

for cwd, dirnames, files in os.walk(os.getcwd()):
	for filename in files:
		fileIn = open(cwd+"/"+filename).read()
		output = Decrypt(fileIn)
		newfilename = filename[:-3]+'_g15612dj.txt'
		os.chdir(outputfolderpath)
		newfile = open(newfilename,'w')
		newfile.write(output)
		newfile.close()