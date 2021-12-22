import sys
import os
from pathlib import Path
import ntpath

# input and output folders
in_dir = sys.argv[1]
out_dir = sys.argv[2]

rugby_scoring = {
	"t" : 5,
	"c" : 2,
	"p" : 3,
	"d" : 3
	}

for in_entry in os.scandir(in_dir):
	# read first line of input file
	rugby_file = open(in_entry.path, 'r')
	rugby_events = rugby_file.readline().strip()
	rugby_file.close()

	score_team1 = 0
	score_team2 = 0

	# program logic
	for i in range(0, int(len(rugby_events)), 3):
		if(rugby_events[i+1] == '1'):
			score_team1 += rugby_scoring[rugby_events[i+2]]
		else:
			score_team2 += rugby_scoring[rugby_events[i+2]]

	# create/write to output file
	out_file_name = Path(in_entry).stem + "_m31234gv.txt"
	out_file_name = os.path.join(out_dir, out_file_name)
	rugby_output_file = open(out_file_name, 'w+')
	rugby_output_file.write(str(score_team1) + ':' + str(score_team2))
	rugby_output_file.close()