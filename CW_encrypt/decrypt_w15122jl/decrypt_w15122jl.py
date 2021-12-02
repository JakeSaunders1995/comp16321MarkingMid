import os
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args=parser.parse_args()
Input=args.input
Output=args.output
info=os.listdir(Input)
oufo=os.listdir(Output)
info.sort()
t=[]
test=''
num=0
test1=''
test2=''
end=''
for file in info:
	f=open(Input+'/'+file)
	test=f.read()
	if test[0]=='H':
		for a in range(0,len(test)):
			if test[a]==' ' and a>3:			
				h=test[a-2:a+1]
				b=chr(int(h,16))
				c=chr(int(test[-2:],16))
				test1+=b
		o=open(Output+'/'+file[0:-4]+'_w15122jl.txt','w')		
		o.write(str.lower(test1+c))
		o.close()
	if test[0]=='C':
		n=18
		while(n)<len(test):										
			cc=test[n]
			if cc==' ':
				test2+=' '
			else:
				ASCII=ord(cc)
				ASCII-=3
				test2+=chr(ASCII)									
			n+=1
		o=open(Output+'/'+file[0:-4]+'_w15122jl.txt','w')		
		o.write(str.lower(test2))
		o.close()
	if test[0]=='M':
		test3=test[11:]
		mlist = {
			    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
			    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
			    '---': 'O', '.--．': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
			    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
			    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
			    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
			    '.-.-.-': '.', '---...': ':', '--..--': ',', '-.-.-.': ';', '..--..': '?',
			    '-...-': '=', '.----.': ''', '-..-.': '/', '-.-.--': '!', '-....-': '-',
			    '..--.-': '_', '.-..-.': ''', '-.--.': '(', '-.--.-': ')', '...-..-': '$',			    
			    }
		ml=test3.split(' ')
		for code in ml:
			code=mlist.get(code,' ').lower()
			end+=code		
		o=open(Output+'/'+file[0:-4]+'_w15122jl.txt','w')		
		o.write(end)
		o.close()