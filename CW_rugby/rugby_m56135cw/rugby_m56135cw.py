#Rugby_v0
import os
import argparse

#Get input&outpus file path from command line.
parser = argparse.ArgumentParser(description = 'Please enter file path')
parser.add_argument('param1', type = str, help = 'absolute input file path')
parser.add_argument('param2', type = str, help = 'absolute output file path')
args = parser.parse_args()

#define a function to check content 
def score(a, b):
	if a == 't': b += 5
	elif a == 'c': b += 2
	elif a == 'p': b += 3
	elif a == 'd': b += 3
	return b

#Get path of input folder.
Input_Files = os.listdir(args.param1)
print(Input_Files)
a = 0
for file in Input_Files:
	if not os.path.isdir(file):
		f = open(args.param1+'/'+file)
		content = f.read()
		f.close()
		print('Match' + str(a) + ":" + content)
		Total_T1 = 0
		Total_T2 = 0

#Calculate final scores.
		for i in range(len(content)):
			if content[i] == '1':
				Total_T1 = score(content[i + 1], Total_T1)
			elif content[i] == '2':
				Total_T2 = score(content[i + 1], Total_T2)

#print winner of each match
		if Total_T1 > Total_T2:
			print('T1 won the match ' + str(a) + '\n')
		elif Total_T1 < Total_T2:
			print('T2 won the match ' + str(a)+ '\n')
		else:
			print('Match ' + str(a) + ' was a draw.'+ '\n')

#write result into output files.
		result = str(Total_T1) + ":" + str(Total_T2)
		out = open(args.param2 + "/" + (Input_Files[a])[:-4] + "_m56135cw.txt",'w')
		a += 1
		out.write(result)
		out.close()

#another solution.
#print(content)
# for i in range(len(content)):
# 	print(content[i])
#finding the content
# T1t = content.count('T1t')
# T2t = content.count('T2t')
# T1c = content.count('T1c')
# T2c = content.count('T2c')
# T1p = content.count('T1p')
# T2p = content.count('T2p')
# T1d = content.count('T1d')
# T2d = content.count('T2d')
# Total_T1 = T1t*5 + T1c*2 + T1p*3 + T1d*3
# Total_T2 = T2t*5 + T2c*2 + T2p*3 + T2d*3