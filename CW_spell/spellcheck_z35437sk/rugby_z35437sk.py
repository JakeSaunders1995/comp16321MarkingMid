# Welcome to Sambbhav's Rugby Match in UOM



import argparse
import os
import sys
import string
import codecs
import glob
def rugby_solver(st):
    team1=False
    team2=False
    score1=0
    score2=0
    for ch in st:
					if(ch=='1'):
						team1=True
						team2=False
						continue
					if(ch=='2'):
						team2=True 
						team1=False
						continue
	
					if(team1==True):
						if(ch=='t'):
							score1+=5
						if(ch=='c'):
							score1+=2
						if(ch=='p'):
							score1+=3
						if(ch=='d'):
							score1+=3
						else:
							continue
					if(team2==True):
						if(ch=='t'):
							score2+=5
						if(ch=='c'):
							score2+=2
						if(ch=='p'):
							score2+=3
						if(ch=='d'):
							score2+=3
						else:
							continue
    return (str(score1)+":"+str(score2)+"\n")
# print(rugby_solver("T1tT2pT2pT1pT1d"))
files=[]
# result=""
if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument('input')
	parser.add_argument('output')
	args = parser.parse_args()
	st=str(args.input)
	st_out=str(args.output)
	l=os.listdir(st)
	l.sort()
	for filepath in l:
		f= os.path.join(st,filepath)
		pos_t=filepath.find(".txt")
		out_fname=filepath[0:pos_t]
		# print(f)
		with codecs.open(f, 'r', encoding='utf-8',errors='ignore') as fdata:
		  string=fdata.read()
		  result=rugby_solver(string)  			
		  with open(os.path.join(st_out,f'{out_fname}_z35437sk.txt'),"w") as file_writer:
		       # print(st_out)
		       file_writer.write(result)
		




# file=argparse.ArgumentParser()
# file.add_argument('input', action='store', type=str,)
# file.add_argument('output', action='append', type=str,)
# args = file.parse_args()
# filepath=[]
# for filepath in os.listdir(sys.argv):

# 		if not(os.path.isfile(filepath)):
# 			continue
# 		for dir,subdir,files,i in os.walk(filepath):
# 			with open(os.path(filepath+files),"r") as file_reader:
# 				st[i]=file_reader.read()
# 				file_reader.close()
# 				print(st)
  				# print(st)
	# f=open("","r")
	# # print(f.read())
	
	# print(len(files))
	# f=open(filepath)
	# st=f.readline()

	

    
# st=args.input



		# ff= os.path.join(path[0]+e,filepath)
		# print(path)
		# # file_writer = open(st_out,"w")
		# # file_writer.write(result)









# for filepath in os.listdir(sys.argv[1]):
# 	if not(os.path.isfile(sys.argv[1]+"/"+filepath)):
# 		continue
# 	with open(os.path.join(os.path.dirname(__file__),sys.argv[1]+"/"+filepath),encoding = 'utf-8') as input_file:
# 	    print(sys.argv[1]+"/"+filepath)
# 	for file in glob.glob(sys.argv[1]+"/"+filepath):
# 		input_file=open(file,"r")
# 		i=input_file.read()
# 		print(i)
# 		result = rugby_solver(i)
# 	files.append(filepath)
		# for k in range (0,len(input)):
		# 	print(input[0], file=outfile, end='')
	# f=open(sys.argv[1]+"/"+filepath,"r")

 #    result=f.read())
	# files.append(filepath)
	# print(filepath)
	# for dir,subdir,file in os.walk(filepath):


	 	# print(result)

# for dir,subdir,file in os.walk(filepath):
#     	infile = open(filepath+file)
#     	outfile = open(savepath,'w')