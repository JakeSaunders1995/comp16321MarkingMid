import sys
import os
import argparse 
the_parser = argparse.ArgumentParser()
the_parser.add_argument('my_input')
the_parser.add_argument('my_output')
args = the_parser.parse_args()
files_input= os.listdir(str(args.my_input))

def finding_score(parameter):
	score_T1=0
	score_T2=0
	while 1:
		inside_info=parameter.read(3)
		if not inside_info:
			break
		if inside_info == 'T1t':
			score_T1+=5
		if inside_info == 'T1c':
			score_T1+=2
		if inside_info == 'T1p':
			score_T1+=3
		if inside_info == 'T1d':
			score_T1+=3
		if inside_info == 'T2t':
			score_T2+=5
		if inside_info == 'T2c':
			score_T2+=2
		if inside_info == 'T2p':
			score_T2+=3
		if inside_info == 'T2d':
			score_T2+=3
		print(inside_info)
		score1=str(score_T1)
		score2=str(score_T2)
		print(score1)
		print(score2)

	with open(files_output, "w") as o:
		o.write(score1 + ':' + score2)



print(files_input)
for g in files_input:
	each_file=str(args.my_input + "/" + g)
	files_output=str(args.my_output + "/" + g[:10] + "_q89254rn" + g[10:])
	with open(each_file, 'r') as i:
		print(i)
		inside=i
		finding_score(inside)
		


