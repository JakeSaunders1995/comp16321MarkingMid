import argparse


my_parser = argparse.ArgumentParser()
#print(my_parser)
my_parser.add_argument('file', type=argparse.FileType('r'))
my_parser.add_argument('secondfile', type=argparse.FileType('w'))
args = vars(my_parser.parse_args())

if args['file']:
	data = args['file'].read()


T1_score = 0
T2_score = 0

split_data = [data[i:i+3] for i in range(0,len(data), 3)]
split_data.pop()
for i in split_data:
	pointType = i[2];
	if i[1] == '1':
		if pointType == 't':
			T1_score += 5
		elif pointType == 'c':
			T1_score += 2
		elif pointType == 'p':
			T1_score += 3
		elif pointType == 'd':
			T1_score += 3
	elif i[1] == '2':
		if pointType == 't':
			T2_score += 5
		elif pointType == 'c':
			T2_score += 2
		elif pointType == 'p':
			T2_score += 3
		elif pointType == 'd':
			T2_score += 3

if T1_score > T2_score:
	print("Team 1 is the winner.")
elif T2_score > T1_score:
	print("Team 2 is the winner.")
else:
	print("Teams drew")

ratio = (str(T1_score) + ":" + str(T2_score))
print("The ratio of T1:T2 is " + ratio)

args['secondfile'].write(ratio)