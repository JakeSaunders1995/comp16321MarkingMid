import sys
import os
import os.path
fn= sys.argv[1]
fo=sys.argv[2]
j=1
for filename in os.listdir(fn):
    if filename.endswith(".txt"):
    	f1=os.path.join(fn,filename)
    	file=open(f1,'rt')
    	f4=filename.index('.txt')
    	f4=filename[0:f4]
    	file1 =open(fo+"/"+f4+"_v12433ak.txt","w")
    	j=j+1
    	s = file.read()
    	length = len(s)
    	score1=0
    	score2=0
    	for i in range(length):
    		if(s[i]=="1"):
    			if(s[i+1]=="t"):
    				score1=score1+5
    			elif(s[i+1]=="c"):
    				score1=score1+2
    			elif(s[i+1]=="p"):
    				score1=score1+3
    			elif(s[i+1]=="d"):
    				score1=score1+3
    		elif(s[i]=="2"):
    			if(s[i+1]=="t"):
    				score2=score2+5
    			elif(s[i+1]=="c"):
    				score2=score2+2
    			elif(s[i+1]=="p"):
    				score2=score2+3
    			elif(s[i+1]=="d"):
    				score2=score2+3
    	file1.write(str(score1)+":"+str(score2))
