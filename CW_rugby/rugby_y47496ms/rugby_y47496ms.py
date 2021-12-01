# Rugby Program

import argparse
import os
from argparse import ArgumentParser

parser = argparse.ArgumentParser()
parser.add_argument('inputs', type=str, help='Input folder')
parser.add_argument('outputs', type=str, help='Output folder')
args = parser.parse_args()

for files in os.listdir(args.inputs):
	if files.endswith(".txt"):
		inputfile = (os.path.join(args.inputs, files))
		files = files[:-4] + "_y47496ms.txt"
		outputfile = (os.path.join(args.outputs, files))

		# Open the files to read

		file = open(inputfile, 'rt')
		input1 = file.read()

		# Initial scores:
		T1 = 0
		T2 = 0

		# Adding to T1's score:
		if "T1t" in input1:
			try1 = input1.count("T1t")
			T1 += (try1 * 5)

		if "T1c" in input1:
			goal1 = input1.count("T1c")
			T1 += (goal1 * 2)

		if "T1p" in input1:
			penalty1 = input1.count("T1p")
			T1 += (penalty1 * 3)

		if "T1d" in input1:
			drop1 = input1.count("T1d")
			T1 += (drop1 * 3)

		# # Adding to T2's score:
		if "T2t" in input1:
			try2 = input1.count("T2t")
			T2 += (try2 * 5)

		if "T2c" in input1:
			goal2 = input1.count("T2c")
			T2 += (goal2 * 2)

		if "T2p" in input1:
			penalty2 = input1.count("T2p")
			T2 += (penalty2 * 3)

		if "T2d" in input1:
			drop2 = input1.count("T2d")
			T2 += (drop2 * 3)

		# T1 and T2 now hold the final scores. Therefore:
		# If T1 > T2, T1 is the winner.
		# If T2 > T1, T2 is the winner.
		# If T1 = T2, the teams have drawn.

		output = open(outputfile, 'wt')
		output.write(str(T1) + ':' + str(T2))
		output.close()
