import os, argparse, re

# take arguments from command line
parser = argparse.ArgumentParser(
	description='Calculates rugby scores')
parser.add_argument('inpath',help='directory containing only .txt files to read input from')
parser.add_argument('outpath',help='directory to write .txt output files to')
args = parser.parse_args()

# prints an error and quits if the input folder doesn't exist, creates the output folder if it doesn't exist
if not os.access(args.inpath,os.F_OK):
	print("Error: Input folder doesn't exist")
	raise SystemExit
if not os.access(args.outpath,os.F_OK):
	os.mkdir(args.outpath)


textfile_pattern = re.compile('^[a-zA-Z0-9_/~]+.txt$')
# loops through files in the provided directory
for file in os.listdir(args.inpath):
	# skips to the next file if the current file is not .txt
	if not textfile_pattern.search(file):
		continue

	# reads the file and splits into an array by the character 'T'
	scores = []
	with open(f'{args.inpath}/{file}') as f:
		scores = f.read().split('T')
	scores.pop(0)

	# creates an array to store the totals and a dictionary for the point allocations
	totals = [0,0]
	points = {'t':5, 'c':2, 'p':3, 'd':3}

	# loops through the scores and adds the relevant points to the correct team's total
	for item in scores:
		totals[int(item[0])-1] += points[item[1]]

	# # outputs the team with the highest score
	# if totals[0] > totals[1]:
	# 	print("Team 1 wins")
	# elif totals[0] < totals[1]:
	# 	print("Team 2 wins")
	# else:
	# 	print("Draw")

	# writes the final totals to the output folder to a file with the same name as the input with username appended
	with open(f'{args.outpath}/{file[:-4]}_w16910dg.txt','w') as f:
		f.write(f"{totals[0]}:{totals[1]}")