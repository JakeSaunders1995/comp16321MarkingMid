import argparse
import os
parser=argparse.ArgumentParser()
parser.add_argument("inputfolder")
parser.add_argument('outputfolder')

args=parser.parse_args()

inputfolder=args.inputfolder 
if(inputfolder[-1]!= '/'):
    inputfolder=inputfolder+'/'

outputfolder=args.outputfolder
if(outputfolder[-1]!='/'):
    outputfolder=outputfolder+'/'

input_files=os.listdir(args.inputfolder)
outputfile=os.listdir(outputfolder)

for file in range(len(input_files)):
	inputfile=open(args.inputfolder+"/"+input_files[file],'r')

	score=inputfile.read()         
	
	scorelist=[]
	n  = 3
	for i in range(0, len(score), n):
		scorelist.append(score[ i: i + n])

	t1,t2=0,0
	for score in scorelist:
		if('T1t' in score):
			t1+=5
		elif('T1c' in score):
			t1+=2
		elif('T1p' in score):
			t1+=3
		elif('T1d' in score):
			t1+=3

		elif('T2t' in score):
			t2+=5
		elif('T2c' in score):
			t2+=2
		elif('T2p' in score):
			t2+=3
		elif('T2d' in score):
			t2+=3



	print("Team T1's score:",t1)
	print("Team T2's score:",t2)



	if(t2>t1):
		print('T2 WINS!')
	elif(t1>t2):
		print('T1 WINS!')

	else:
		print("Draw!")

	t1score=str(t1)
	t2score=str(t2)
	result= t1score+':'+t2score

	outputfile=open(str(outputfolder)+str((input_files[file])[0:(len(input_files[file])-4)])+'_u60328el'+".txt",'w')
	outputfile.write(result)














   