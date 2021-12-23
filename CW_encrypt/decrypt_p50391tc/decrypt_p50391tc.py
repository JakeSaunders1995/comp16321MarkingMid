
file= open('test_file1.txt','r')
filecontent=file.read()


hexa={'61':'a','62':'b','63':'c',
'64':'d','65':'e','66':'f',
'67':'g','68':'h','69':'i',
'6a':'j','6b':'k','6c':'l',
'6d':'m','6e':'n','6f':'o',
'70':'p','71':'q','72':'r',
'53':'s','73':'s','74':'t','75':'u',
'76':'v','77':'w','78':'x',
'79':'y','7a':'z'}

caesar={'d':'a','e':'b','f':'c',
'g':'d','h':'e','i':'f',
'j':'g','k':'h','l':'i',
'm':'j','n':'k','o':'l',
'p':'m','q':'n','r':'o',
's':'p','t':'q','u':'r',
'v':'s','w':'t','x':'u',
'y':'v','z':'w','a':'x',
'b':'y','c':'z'}

morse={'.-':'a', '-...':'b', '-.-.':'c',
'-..':'d', '.': 'e', '..-.': 'f',
'--.': 'g', '....':'h', '..':'i',  
'.---': 'j', '-.-': 'k', '.-..': 'l',
'--': 'm',  '-.': 'n',  '---': 'o', 
'.--.': 'p', '--.-': 'q', '.-.': 'r',
'...': 's', '-': 't', '..-': 'u', 
'...-': 'v', '.--': 'w', '-..-': 'x',
'-.--': 'y', '--..': 'z'}

if 'Hex' in filecontent:
	print('The encryption method is Hexadecimal.')
	engword = []
	engletter = []
	j = -1
	for i in filecontent.split():
		j += 1
		engletter += [i.split()]
		for k in range(len(engletter[j])):
			engword += hexa.get(engletter[j][k],' ')
			engword += ''


elif 'Caesar Cipher(+3)' in filecontent:
	print('The encryption method is Caesar +3.')
	engword=''
	for i in filecontent:
		if (i== ' '):
			engword+= ' '
		else:
			engword += (chr(ord(i) - 3))

elif 'Morse Code' in filecontent:
	print('The encryption method is Morse Code.')
	engword = []
	engletter = []
	j = -1
	for i in filecontent.split():
		j += 1
		engletter += [i.split()]
		for k in range(len(engletter[j])):
			engword += morse.get(engletter[j][k],' ')
			engword += ''



f=open('test_file1_p50391tc.txt','w')
f.write(''.join(engword))