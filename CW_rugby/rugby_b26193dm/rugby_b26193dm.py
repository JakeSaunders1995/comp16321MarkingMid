import os
import argparse
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("put_in_file", help="Enter a file")
	parser.add_argument("put_out_file", help="Enter a file")
args = parser.parse_args()
input_file = args.put_in_file
for j in os.listdir(input_file):
	text_pos = j.find('.txt')
	input_file_heading = j[0:text_pos]
	file = open(f'{args.put_in_file}/{j}', 'r')
	T1 = 0
	T2 = 0
	B = 0
	while 1:
		a = file.read(1)
		if not a:
			break
		if B == 1:
			if a == 't':
				T1 = T1 + 5
				B = 0
			elif a == 'c':
				T1 = T1 + 2
				B = 0
			elif a == 'p':
				T1 = T1 + 3
				B = 0
			elif a=='d':
				T1 = T1 + 3
				B = 0
		elif B == 2:
			if a == 't':
				T2 = T2 + 5
				B = 0
			elif a == 'c':
				T2 = T2 + 2
				B = 0
			elif a == 'p':
				T2 = T2 + 3
				B = 0
			elif a == 'd':
				T2 = T2 + 3
				B = 0
		elif a == 'T':
			B = 0
#			a = 0
		elif a == '2':
			B = 2
		elif a == '1':
			B = 1

	final = f'{T1}:{T2}'
	result = ""
	if T1>T2:
		result = "T1 is the winner"
	elif T2>T1:
		result = "T2 is the winner"
	else:
		result = "It's a draw"
	#print(final, result)

	# Final Result
	line = [f'{T1}:{T2}']
	with open(os.path.join(args.put_out_file, f'{input_file_heading}_b26193dm.txt'), 'w') as f:
		f.writelines(line)

