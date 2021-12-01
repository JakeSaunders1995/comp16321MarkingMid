


import sys
import glob
import os
import re
file1=sys.argv[1]
file2=sys.argv[2]


path = os.path.abspath(file1)
files = glob.glob(path + "/*.txt")

for file in files:
	with open(file) as f:
		text=f.read()
		print(text)




#d = {'T1t':'a' , 'T1c':'b' , 'T1p':'c' , 'T1d':'d', 'T2t':'e', 'T2c':'f' , 'T2p':'g' , 'T2d':'h'}
#tbl = str.maketrans(d)

#b = 2 
#d = 3 
#f = 2 
#g = 3 
#h = 3

#text2 = text.translate(tbl) 

#print(text2)

tcpd = {'t': 5, 'c': 2, 'p': 3, 'd':3}

score = {}

for type, t in re.findall('(T\d)(.)', text):
    score[type] = score.get(type, 0) + tcpd.get(t, 0)

print(score)

path = os.path.abspath(file2)
newfile =open("text_file_b05899em.txt", "w")
newfile.write("score")
newfile.close()
#s=f.close()

#with open(files) as f:
#score = {}

#t1 = {'T1t':5 , 'T1c':2 , 'T1p':3 , 'T1d':3, 'T2t':5 , 'T2c':2 , 'T2p':3 , 'T2d':3 }

#for type, t in re.findall('T2(.)', text):
	#score[type] = score.get(type,0) + t1.get(t,0)


#print(score)
































