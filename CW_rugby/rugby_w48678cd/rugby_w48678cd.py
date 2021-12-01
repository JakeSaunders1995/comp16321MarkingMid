import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument(dest='argument1', help="This is the Input File")
parser.add_argument(dest='argument2', help="This is the Output File")
args = parser.parse_args()

FolderInput=args.argument1
FolderOutput=args.argument2
t=5
c=2
p=3
d=3

for FileInput in os.listdir(FolderInput):
	In_fname=os.path.basename(FileInput)
	In_filepath = os.path.join(FolderInput, In_fname)
	if os.path.isfile(In_filepath):
		fileIn, extension = os.path.splitext(FileInput)

		T1_Score=0
		T2_Score=0
		score=0
		TeamScores=[]

		scores=open(In_filepath,"r")
		text=scores.readline()
		text=text.strip()
		scores.close()
		for index in range(0,len(text),3):
			TeamScores.append(text[index:index+3])
		for n in range(0,len(TeamScores)):
			if TeamScores[n][2]=="t":
				score=t
			elif TeamScores[n][2]=="c":
				score=c
			elif TeamScores[n][2]=="p":
				score=p	
			elif TeamScores[n][2]=="d":
				score=d		
			if "T1" in TeamScores[n]:
				T1_Score=T1_Score+score		
			elif "T2" in TeamScores[n]:
				T2_Score=T2_Score+score
		Outfname=os.path.basename(FileInput)
		filename, file_extension = os.path.splitext(Outfname)
		fname=filename+"_w48678cd"+file_extension
		filepath = os.path.join(FolderOutput, fname)

		result=open(filepath,"w")
		result.write(str(T1_Score)+":"+str(T2_Score))
		result.close()
	elif os.path.isdir(In_filepath):
		print("Folder within it ignored")
	else:
		print("Unoknow file ignored")
