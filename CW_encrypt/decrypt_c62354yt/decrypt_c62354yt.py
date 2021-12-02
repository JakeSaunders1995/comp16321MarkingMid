import sys
import os

filepath=""
outputpath=""
outputname=""
entext=""
entype=""
detext=""
caec="zyxwvutsrqponmlkjihgfedcbazyx"
alpha="abcdefghijklmnopqrstuvwxyz"
ALPHA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
morc={".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i",
 ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t",
 "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z",  ".-.-.-":".",
  "..--..":"?", "-.-.--":"!", "--..--":",", "---...":":", "-....-":"-", "-.--.":"(", "-.--.-":")",
   ".----.":"'", ".-..-.":'"', "/":" ", "-.-.-.":";"}

folder=sys.argv[1]
if folder[0]=="." and folder[1]=="/":
	folder=folder.replace("./","",1)
outputpath=sys.argv[2]
if outputpath[0]=="." and outputpath[1]=="/":
	outputpath=outputpath.replace("./","",1)
filelist=os.listdir(folder)
for i in range (len(filelist)):
	check=filelist[i]
	if check.endswith(".txt"):
		filepath=str(folder)+"/"+str(filelist[i])
		file=open(filepath, "r")
		txt=file.read()
		for j in range(0,3):
			entype=entype+txt[j]
		for m in range(len(txt)):
			if txt[m]==":":
				x=m+1
		


		if entype=="Mor":
			for k in range(x,len(txt)):
				if txt[k]==" ":
					detext=str(detext)+str(morc[entext])
					entext=""
					continue
				entext=str(entext)+str(txt[k])
			if entext!="":
				detext=str(detext)+str(morc[entext])
		elif entype=="Cae":
			for k in range(x,len(txt)):
				for l in range(len(caec)-1):
					if txt[k]==caec[l]:
						detext=str(detext)+caec[l+3]
				if txt[k]==" ":
					detext=str(detext)+str(" ")
		elif entype=="Hex":
			for k in range(x,len(txt)):
				if txt[k]==" ":
					hextoint=int(entext,16)
					detext=str(detext)+chr(hextoint)
					entext=""
					continue
				entext=str(entext)+str(txt[k])
			if entext!="":
				hextoint=int(entext,16)
				detext=str(detext)+chr(hextoint)
		
		outputname=str(outputpath)+"/"+str(check.replace(".txt","_c62354yt.txt"))
		output=open(outputname, "w")
		output.write(detext)
		output.close()
		entext=""
		entype=""
		detext=""