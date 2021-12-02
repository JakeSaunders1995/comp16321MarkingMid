import sys
import argparse
import os

def file_name(file_dir):
	files=os.listdir(file_dir)
	return files

parser = argparse.ArgumentParser()
parser.add_argument("read_space", help="display a name of a table")
parser.add_argument("write_space", help="display a name of a space")
args = parser.parse_args()
numberlist=["1","2","3","4","5","6","7","8","9","0"]
MorseList = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
    "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n",
    "---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
    "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

    ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
    "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
    "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
     ".--.-.": "@", ".-.-.": "+",
}

x=file_name(args.read_space)
for i in x:
	a=[]
	name=""
	wordlist=[]
	for h in i:
		wordlist.append(h)
	list2=wordlist[:-4]
	for g in list2:
		name+=g
	with open(args.read_space+"/"+i,'r') as f:
		g=(f.read())
		a.append(g)

	if a[0][0]=="H" or a[0][0] in numberlist:
	    b=a[0].split(" ")
	    if len(b[0])>2:
	    	c=b[0].split(":")
	    	b.pop(0)
	    	b.insert(0,c[1])
	    ans=""	
	    num=0
	    for i in b:
	    	num=int(i, 16)
	    	word=chr(num)
	    	ans+=word


	elif a[0][0]=="M" or a[0][0]=="." or a[0][0]=="-":
		ans=""
		b=a[0].split("/")
		list1=[]
		for i in range(len(b)):
			x=b[i].strip("Morse Code:")
			list1.append(x)
		for h in list1:
			y=h.split(" ")
			for g in y:
				ans+=MorseList[g]
			ans+=" "






	else:
		words=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
		"r","s","t","u","v","w","x","y","z"]
		b=a[0].split(" ")
		if "Caesar" in b:
			b.remove("Caesar")
		if ":" in b[0]:
			c=b[0].split(":")
			b.pop(0)
			b.insert(0,c[1])
		ans=""
		for i in b:
			for j in i:
				if j in words:
					if j=="a":
						ans+="x"
					elif j=="b":
						ans+="y"
					elif j=="c":
						ans+="z"
					else:
						for x in range(len(words)):	
							if words[x]==j:
								ans+=words[x-3]
			ans+=" "


	fs = open(args.write_space+"/"+name+"_z16075sc.txt",'w')
	fs.write(ans.lower())


