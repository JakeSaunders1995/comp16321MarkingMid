import argparse 
import os

path = argparse.ArgumentParser()
path.add_argument("input_path")
path.add_argument("output_path")

file = path.parse_args()
for infiles in os.listdir(file.input_path):
	Input = open(file.input_path + "/" +infiles, "r")
	t = list(file.output_path + "/" +infiles)
	for i in range (4):
		t.pop(-1)
	t = ("").join(t)
	filename = t + "_b03791zc"
	filepath = os.path.join(file.output_path, filename)
	Output = open(filepath, "w")

	score_p = Input.readlines()
	scores = list(score_p[0])
	T1 = 0
	T2 = 0
	for i in range (int(len(scores)/3)):
		if scores[(3*i)+1] == "1":
			if scores[(3*i)+2] == "t":
				T1 += 5
			elif scores[(3*i)+2] == "c":
				T1 += 2
			elif scores[(3*i)+2] == "p" or scores[(3*i)+2] == "d":
				T1 += 3
		elif scores[(3*i)+1] == "2":
			if scores[(3*i)+2] == "t":
				T2 += 5
			elif scores[(3*i)+2] == "c":
				T2 += 2
			elif scores[(3*i)+2] == "p" or scores[(3*i)+2] == "d":
				T2 += 3
	final = (str(T1),":",str(T2))
	Output.writelines(final)
	Input.close()
	Output.close()