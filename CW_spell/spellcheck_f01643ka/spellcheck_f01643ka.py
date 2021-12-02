import os.path
import sys
inputfolder = sys.argv[2]
output = sys.argv[3]
dic = sys.argv[1]
for filename in os.listdir(inputfolder):
	fpath = inputfolder + "/" + filename
	filetxt= open(fpath, "r")
	file = filetxt.read()
	num = 0
	pun = 0
	cap = 0
	ntext = ""
	sen = "f01643ka\n"
	sen += "Formatting ###################\n"
	j =0
	sp = 0
	r = 0
	v =0
	co = 0
	for i in file:
		for j in i:
			co+=1
			if (58 > ord(i) > 47):
				num +=1
			elif (32 < ord(i) < 48) or (57 < ord(i) < 64) or (90 < ord(i) < 97) or (122 < ord(i) < 127):
				pun += 1
				if(ord(i)==46):
					if co != len(file) and i == file[co+1] and i == file[co+2]:
						pun-=2
			elif (64 < ord(i) < 91):
				cap+=1
				ntext+=i
			else:
				ntext += i
		ntext = ntext.lower()
	sen+= "Number of upper case letters changed: " + str(cap) + "\n"
	sen+= "Number of punctuations removed: " + str(pun) + "\n"
	sen+= "Number of numbers removed: " + str(num) + "\n"
	sen+= "Spellchecking ###################\n"
	words = ntext.split(" ")
	for x in ntext.split(" "):
		if x in dic:
			r+=1
		else: 
			sp+= 1
	summ = sp + r
	sen+= "Number of words: " + str(summ) + "\n"
	sen+= "Number of correct words: " + str(r) + "\n"
	sen+= "Number of incorrect words:" + str(sp)
	outfile = output + "/" + filename[0:10] +"_f01643ka" + ".txt"
	tempout = open(outfile, "w")
	tempout.write(sen)
	tempout.close()






