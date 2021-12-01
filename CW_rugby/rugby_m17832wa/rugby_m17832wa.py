import sys, re, os

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if input_folder[-1] != "/":
	input_folder += "/"
if output_folder[-1] != "/":
	output_folder += "/"

input_files = os.listdir(input_folder)

for file in range(len(input_files)):
	file_input = open(input_folder + input_files[file], 'r')
	file_contents = file_input.readlines() # could try read

	t1_score = t2_score = 0

	for line in range(len(file_contents)):
		scores = re.split("T", file_contents[line]) # if trying read change this

		for score in scores:
			if "1" in score:
				if "t" in score:
					t1_score += 5
				elif "c" in score:
					t1_score += 2
				elif "p" in score:
					t1_score += 3
				elif "d" in score:
					t1_score += 3
				else:
					pass
			elif "2" in score:
				if "t" in score:
					t2_score += 5
				elif "c" in score:
					t2_score += 2
				elif "p" in score:
					t2_score += 3
				elif "d" in score:
					t2_score += 3
				else:
					pass
			else:
				pass

	output_for_file = str(t1_score) + ":" + str(t2_score)

	fileName = str(input_files[file]).replace('.txt', '')
	output_file_loc = output_folder + fileName + "_m17832wa.txt"
	output_file = open(output_file_loc, "w")
	output_file.write(output_for_file)

	output_file.close()