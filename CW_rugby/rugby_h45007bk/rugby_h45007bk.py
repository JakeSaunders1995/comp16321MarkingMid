def main(input_filepath,output_filepath):

    score_points={
        't':5,
        'c':2,
        'p':3,
        'd':3
    }
    file=open(input_filepath,'r')
    scores=file.read().strip()
    file.close()
    final_score=[0,0]

    # T 1/2 t/c/p/d

    assert len(scores)%3==0, 'Scores file in wrong format.'
    for i in range(0, len(scores),3):
        assert scores[i]=='T', 'Scores file in wrong format.'
        team=int(scores[i+1])-1
        assert team==0 or team==1, "Scores file in wrong format."
        scr_tp=scores[i+2]
        scr_n=score_points[scr_tp] #will throw keyError if not a type of score
        final_score[team]+=scr_n

    print("for match in file "+args.input_path+" the outcome was: ")
    if final_score[0]==final_score[1]:
        print("The match was a draw.")
    else:
        print("Winner: ",end='')
        if final_score[0]>final_score[1]:
            print("Team 1")
        else:
            print("Team 2")
    print()

    fw_str=str(final_score[0])+':'+str(final_score[1])
    file=open(output_filepath,'w')
    file.write(fw_str)
    file.close()

#--------

#to iterate over txt files in a directory, (non recusrively)
#or just files if given paths to files

import argparse, os
parser=argparse.ArgumentParser(description="Script to calculate final score of a rugby match from a list of match scores")
parser.add_argument('input_path',type=str,help="Input path to file or folder")
parser.add_argument('output_path',type=str,help="Output path to file or folder")

args=parser.parse_args()

username='_h45007bk'

def dir_txtlist(dirpath):
	f_list=[]
	for f_obj in os.scandir(dirpath):
		if f_obj.is_file(follow_symlinks=True):
			f_list.append(f_obj.path)
	return f_list

if not os.path.exists(args.input_path):
	print("Error: cannot access or find the input path at this time.")
	exit()

if os.path.isdir(args.input_path):
	if not os.path.exists(args.output_path):
		os.makedirs(args.output_path)
	if os.path.isdir(args.output_path):
		fin_lst=dir_txtlist(args.input_path)
		for fileout in fin_lst:
			fout=os.path.join(args.output_path,os.path.basename(fileout))
			ext_i=fout.rfind('.')
			fout=fout[:ext_i]+username+fout[ext_i:]
			fin=os.path.join(args.input_path,os.path.basename(fileout))
			main(fin, fout)
	else:
		print('Error: output path must be to a directory if the input path is also to a directory')
		exit()
elif os.path.isfile(args.input_path):
	if os.path.isdir(args.output_path):
		fout=os.path.join(args.output_path,os.path.basename(args.input_path))
		ext_i=fout.rfind('.')
		fout=fout[:ext_i]+username+fout[ext_i:]
		main(args.input_path, fout)
	elif os.path.isfile(args.output_path) or (not os.path.exists(args.output_path)):
		main(args.input_path, args.output_path)

else:
	print("Error: provided path(s) are not to a file or directory")
	exit()
