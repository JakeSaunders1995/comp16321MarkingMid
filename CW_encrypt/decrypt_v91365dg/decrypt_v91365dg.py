import os
import sys
tRoute=["t",[["m",[ ["o",[["",["0","9"]],["",["","8"]] ]],["g",[["q"],["z",["","7"]]]] ]],["n",[["k",["y","c"]],["d",["x",["b",["","6"]]]]] ] ]]
eRoute=["e",[["a",[["w",[["j",["1",""]],["p"]] ],["r",["0","l"]]]],["i",[["u",[["",["2"]],["f"]]],["s",[["v",["3"]],["h",["4","5"]]]] ]] ]] 
Alphabet="abcdefghijklmnopqrstuvwxyzabc"
def MorseDecode(Code):
	Letter=""
	if(Code=="."):
		Letter="e"
	elif(Code=="-" or Code=="_"):
		Letter="t"
	elif(Code=="/"):
		Letter=" "
	else:
		if(Code[0]=="."):
			CurrentTree=eRoute
		else:
			CurrentTree=tRoute
		for j in range(1,len(Code)):
			CurrentTree=CurrentTree[1]
			if(Code[j]=="."):
				CurrentTree=CurrentTree[1]
			elif(Code[j]=="-" or Code[j]=="_"):
				CurrentTree=CurrentTree[0]
		Letter=str(CurrentTree[0])
	return Letter
for File in os.listdir(sys.argv[1]):
	InputFile=open(os.path.join(sys.argv[1],File),"r")
	Text=InputFile.read()
	Found=False
	Function=""
	counter=0
	while(Found==False):
		if(Text[counter]==":"):
			Found=True
		else:
			Function+=Text[counter]
		counter+=1
	CipheredText=""
	if(Function=="Hex"):
		CipheredText=bytearray.fromhex(Text[counter:len(Text)]).decode()
	else:
		Word=""
		for i in range(counter,len(Text)):
			if(Function=="Caesar Cipher(+3)"):
				Counter=len(Alphabet)-1
				Found=False
				while Counter>0 and Found==False:
					if(Text[i]==Alphabet[Counter]):
						Letter=Alphabet[Counter-3]
						CipheredText+=Letter
						Found=True
					Counter-=1
				if(Found==False):
					CipheredText+=Text[i]
			elif(Function=="Morse Code"):
				if(Text[i]=="/"):
					Word="/"
				elif(Text[i]==" "):
					Letter=MorseDecode(Word)
					CipheredText+=Letter
					Word=""
				else:
					Word+=Text[i]
				if(i==len(Text)-1):
					if(len(Word)>0):
						Letter=MorseDecode(Word)
						CipheredText+=Letter
	CipheredText=CipheredText.lower()
	OutputFile=open(os.path.join(sys.argv[2],File[0:len(File)-4]+'_v91365dg.txt'),"w")
	OutputFile.write(CipheredText)
	OutputFile.close()
