import os
import os.path
import sys
morseCode = {
'.-' : 'A',
'-...' : 'B',
'-.-.' : 'C',
'-..' : 'D',
'.' : 'E',
'..-.': 'F',
'--.': 'G',
'....' : 'H',
'..' : 'I',
'.---': 'J',
'-.-' : 'K',
'.-..': 'L',
'--' : 'M',
'-.': 'N',
'---' : 'O',
'.--.': 'P',
'--.-': 'Q',
'.-.' : 'R',
'...' : 'S',
'-' : 'T',
'..-' : 'U',
'...-' : 'V',
'.--' : 'W',
'-..-': 'X',
'-.--' : 'Y',
'--..': 'Z',
'-----' : 'O',
'.----' : '1',
'..---' : '2',
'...--' : '3',
'....-' : '4',
'.....' : '5',
'-....' : '6',
'--...' : '7',
'---..' : '8',
'----.' : '9',
'--..--': ',' ,
'.-.-.-' :  '.' ,
'..--..' : '?' ,
'-..-.'  :  '/' ,
'-....-' :  '-' ,
'-.--.' : '(' ,
'-.--.-' :  ')'
}

inputDir = sys.argv[1]
outputDir = sys.argv[2]
for filename in os.listdir(inputDir):
	file = open(inputDir+"/"+filename, 'r')
	text = file.read()
	outputfname = filename[:-4]
	pathF = outputDir
	translation = ''
	index = text.index(':')
	for i in text:
		if i == ':':
			msg = text[index+1:]

	def cipher2eng():
		global msg , translation
		translation= ''
		for i in range(len(msg)):
			if msg[i] == ' ':
				translation += msg[i]
			elif msg[i] == 'a':
				translation += 'x'
			elif msg[i] == 'b':
				translation += 'y'
			elif msg[i] == 'c':
				translation += 'z'
			elif 19 < ord(msg[i])-3:
				translation += chr(ord(msg[i])-3)
		return translation
	def morse2eng():
		global msg , translation
		msgList = msg.split()
		for code in msgList:
			if code in morseCode.keys():
				value = morseCode[code]
				translation +=  value
			else:
				translation+= ' '

		return translation.lower()

	def main():
		global msg , translation
		if text.startswith('H'):
			translation = bytes.fromhex(msg).decode('utf-8')
			outputf = outputDir + '/' + filename[0:-4] + '_' + 'v21023jh.txt'
			output = open(outputf,'w')
			output.write(str(translation.lower()))
			output.close()
		elif text.startswith('C'):
			translation = cipher2eng()
			outputf = outputDir + '/' + filename[0:-4] + '_' + 'v21023jh.txt'
			output = open(outputf,'w')
			output.write(str(translation))
			output.close()
		elif text.startswith('M'):
			translation = morse2eng()
			outputf = outputDir + '/' + filename[0:-4] + '_' + 'v21023jh.txt'
			output = open(outputf,'w')
			output.write(str(translation))
			output.close()

	if not os.path.exists(pathF):
		os.makedirs(pathF)
	main()
