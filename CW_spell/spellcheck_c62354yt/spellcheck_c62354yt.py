import sys
import os

filepath=""
outputpath=""
outputname=""
ewfile=""
engwords=[]
alpha="abcdefghijklmnopqrstuvwxyz"
ALPHA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word=""
wordlist=[]
num="0123456789"
ALPHAno=0
numno=0
puncno=0
correct=0
ccheck=0
wrong=0
alphacheck=0
numcheck=0
puna=""
punb=""
punc=""
a=0
b=0
c=0

ewfile=sys.argv[1]
if ewfile[0]=="." and ewfile[1]=="/":
	ewfile=ewfile.replace("./","",1)
eng=open(ewfile)
for line in eng:
	line=line.rstrip()
	engwords.append(line)
eng.close()

folder=sys.argv[2]
if folder[0]=="." and folder[1]=="/":
	folder=folder.replace("./","",1)

outputpath=sys.argv[3]
if outputpath[0]=="." and outputpath[1]=="/":
	outputpath=outputpath.replace("./","",1)

filelist=os.listdir(folder)
for i in range (len(filelist)):
	check=filelist[i]
	if check.endswith(".txt"):
		filepath=str(folder)+"/"+str(filelist[i])
		file=open(filepath, "r")
		txt=file.read()

		for j in range(len(txt)):
			alphacheck=0
			for k in range(len(alpha)):
				if txt[j]==alpha[k]:
					word=str(word)+str(txt[j])
					alphacheck-=1
					break
				elif txt[j]==ALPHA[k]:
					txt.replace(ALPHA[k],alpha[k],1)
					ALPHAno+=1
					word=str(word)+str(alpha[k])
					alphacheck-=1
					break
				elif txt[j]==" ":
					if word!="":
						wordlist.append(word)
						word=""
						alphacheck-=1
						break
				alphacheck+=1
				if alphacheck==len(alpha):
					numcheck=0
					for l in range(len(num)):
						if txt[j]==num[l]:
							numno+=1
							numcheck+=1
							break
					if numcheck==0 and txt[j]!="" and txt[j]!=" " and txt[j]!="\n":
						puncno+=1
						puna=punb
						punb=punc
						punc=txt[j]
						a=b
						b=c
						c=j
						if puna=="." and punb=="." and punc==".":
							if c==b+1 and b==a+1:
								puncno-=2
						numcheck=0
					txt.replace(txt[j],"",1)
					break
		if word!="":
			wordlist.append(word)
			word=""
		print(txt)

		for m in range(len(wordlist)):
			for n in range(len(engwords)):
				if wordlist[m]==engwords[n]:
					correct+=1
					break
			if correct!=ccheck:
				ccheck=correct
			else:
				wrong+=1
				ccheck=correct
		
		line1="\nFormatting ###################"
		line2="\nNumber of upper case letters changed: "+str(ALPHAno)
		line3="\nNumber of punctuations removed: "+str(puncno)
		line4="\nNumber of numbers removed: "+str(numno)
		line5="\nSpellchecking ###################"
		line6="\nNumber of words: "+str(len(wordlist))
		line7="\nNumber of correct words: "+str(correct)
		line8="\nNumber of incorrect words: "+str(wrong)

		outputname=str(outputpath)+"/"+str(check.replace(".txt","_c62354yt.txt"))
		output=open(outputname, "w")
		output.write("c62354yt")
		output.write(line1)
		output.write(line2)
		output.write(line3)
		output.write(line4)
		output.write(line5)
		output.write(line6)
		output.write(line7)
		output.write(line8)
		output.close()

		wordlist=[]
		ALPHAno=0
		numno=0
		puncno=0
		correct=0
		ccheck=0
		wrong=0
		alphacheck=0