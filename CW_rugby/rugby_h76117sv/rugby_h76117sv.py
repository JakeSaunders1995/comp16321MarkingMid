import argparse
import os

def get_output_file_name(filename, username):
	before_txt = filename.split('.')[0]
	return before_txt + '_' + username + '.txt'

string=""
if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument('input')
	parser.add_argument('output')
	args=parser.parse_args()
var = str(args.input)
out=str(args.output)
m=os.scandir(var)
for filepath in m:
	f=os.path.join(var,filepath)
	string=open(filepath, 'r') 
	string=string.read()
	
	length=len(string)
	points={
	't': 5,
	'c': 2,
	'p':3,
	'd':3
	}
	totalT1=0
	totalT2=0
	for i in range (length):
		charac=string[i]
		if charac=='T':
			i=i+1
			team=string[i]
			if team=='1':
				i=i+1
				for x,y in points.items():
					if(x==string[i]):
						totalT1=totalT1+y
			elif team=='2':
				i=i+1
				for p,q in points.items():
					if(p==string[i]):
						totalT2=totalT2+q
		
	output_file = os.path.join(args.output, get_output_file_name(filepath.name, 'h76117sv'))
	with open(output_file,'w+') as file:
	 	file.write(str(totalT1) + ":"+str(totalT2))



		
