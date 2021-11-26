import argparse
import os

parser = argparse.ArgumentParser(description = 'Score calculator')
parser.add_argument('input', help = 'Enter input path')
parser.add_argument('output', help = 'Enter output path')
args = parser.parse_args()

input1 = args.input
output = args.output

directory = input1
count = 0
for filename in os.scandir(directory):
	if filename.is_file():
		file = open(filename)
		list1 = file.read()

	def scoringt1():
		score = 0
		for i in range(len(list1)):
			if(list1[i].islower() == True and list1[i-1] == "1"):
				if list1[i] == "t":
					score +=5
				elif list1[i] == "c":
					score +=2
				elif list1[i] == "p":
					score +=3
				elif list1[i] == "d":
					score +=3
		return score

	def scoringt2():
		score = 0
		for i in range(len(list1)):
			if(list1[i].islower() == True and list1[i-1] == "2"):
				if list1[i] == "t":
					score +=5
				elif list1[i] == "c":
					score +=2
				elif list1[i] == "p":
					score +=3
				elif list1[i] == "d":
					score +=3
		return score

	d = os.path.basename(filename)
	x = os.path.splitext(d)[0]
	name = os.path.join(output,str(x)+"_q53226rb.txt")
	file2 = open(name,"a")
	file2.write(str(scoringt1())+":"+str(scoringt2()))
	file2.close
