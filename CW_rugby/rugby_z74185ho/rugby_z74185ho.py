import sys, os, argparse, re

parser = argparse.ArgumentParser()
parser.add_argument("inputpath", type=str)
parser.add_argument("outputpath", type=str)
args = parser.parse_args()

cwd = os.getcwd()

for dirpath, dirnames, filenames in os.walk(args.inputpath):
	for file in filenames:
		# print(file)
		if file.endswith(".txt"):
			targetfile = os.path.join(os.path.relpath(dirpath, cwd),file)
			with open(targetfile,'r') as f:
				line = f.read()
			scores = line.split("T")
			scores.remove("")
			# print(scores)

			t1 = []
			t2 = []

			for i in scores:
				if (i[0] == "1"):
					t1.append(i)
				elif (i[0] == "2"):
					t2.append(i)
			# print(t1)
			# print(t2)

			t1score = 0
			t2score = 0

			for n in t1:
				if (n[1] == "t"):
					t1score += 5
				elif (n[1] == "c"):
					t1score += 2
				elif (n[1] == "p"):
					t1score += 3
				elif (n[1] == "d"):
					t1score += 3
				else:
					continue

			for m in t2:
				if (m[1] == "t"):
					t2score += 5
				elif (m[1] == "c"):
					t2score += 2
				elif (m[1] == "p"):
					t2score += 3
				elif (m[1] == "d"):
					t2score += 3
				else:
					continue

			# print(t1score)
			# print(t2score)

			FileName = file.split(".")
			outputFileName = FileName[0] + "_z74185ho." + FileName[1]
			outputFilePath = os.path.join(args.outputpath, outputFileName)

			with open(outputFilePath, "w") as of:
				of.write(str(t1score) + ":" + str(t2score))

			continue

		else:
			continue








