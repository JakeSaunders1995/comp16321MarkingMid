import os,sys 
inputfile=sys.argv[1]
path1=os.listdir(inputfile)
outputfile=sys.argv[2]


def winner():
	for file in range(len(path1)):
		name_input=path1[file]
		a=os.path.join(inputfile,name_input)
		file1=open(a,"r")
		name=""
		for letter in name_input:
			if letter==".":
				break
			else:
				name+=letter
		name_output=name+"_t30023mm"
		b=os.path.join(outputfile,name_output)
        
		file2=open(b,"w")

		ctr=0
		T1_score=0
		T2_score=0
		for i in file1.readlines():
			line = list(i)
			while ctr<len(line)-1:
				if line[ctr+1]=="1":
					x=line[ctr+2]
					total = score(x)
					T1_score+=total
					ctr+=3
				elif line[ctr+1] in "2":
					x=line[ctr+2]
					total = score(x)
					T2_score+=total
					ctr+=3
		final_score = str(T1_score) + ':' + str(T2_score)
		#print(final_score)	
		file2.write(final_score)
		#if T1_score>T2_score:
		#	print("T1 is winner")
		#elif T2_score>T1_score:
		#	print("T2 is winner")
		#else:
		#	print("Draw")

	


def score(x):
	if x=='t':
		return 5
	elif x=='c':
		return 2
	elif x=='p':
		return 3
	elif x=='d':
		return 3

winner()