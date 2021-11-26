import os
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")

args = parser.parse_args()

inputfolderpath = (args.input_folder_path)
outputfolderpath = (args.output_folder_path)

for filename in os.listdir(inputfolderpath):
	if filename.endswith(".txt"):
		inputfile = open(inputfolderpath + "/" + filename)
		score = inputfile.readline()

		T1 = 0
		T2 = 0

		i = 0

		while i < len(score):
			if "T1t" in score[i:i+3]:
				T1 = T1 + 5
			elif "T1c" in score[i:i+3]:
				T1 = T1 + 2
			elif "T1p" in score[i:i+3]:
				T1 = T1 + 3
			elif "T1d" in score[i:i+3]:
				T1 = T1 + 3
			elif "T2t" in score[i:i+3]:
				T2 = T2 + 5
			elif "T2c" in score[i:i+3]:
				T2 = T2 + 2
			elif "T2p" in score[i:i+3]:
				T2 = T2 + 3
			elif "T2d" in score[i:i+3]:
				T2 = T2 + 3
			i = i + 3


		temp = filename.split(".")
		output_file_name = temp[0] + "_" + "f13855hl" + "." + temp[1]
		outputFile = open(outputfolderpath + "/" + output_file_name, "w")
		outputFile.write(str(T1) + ":" + str(T2))
		outputFile.close()
