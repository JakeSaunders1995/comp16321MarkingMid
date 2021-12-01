import os, sys


def calculate(string):
	t1 = 0
	t2 = 0

	for i, char in enumerate(string):
		if i % 3 == 2:
			if char == "t":
				score = 5
			elif char == "c":
				score = 2
			else:
				score = 3

			if string[i - 1] == "1":
				t1 += score
			else:
				t2 += score

	return f"{t1}:{t2}"


for filename in os.listdir(sys.argv[1]):
	if filename.endswith(".txt"):
		file = open(f"{sys.argv[1]}/{filename}")
		string = file.readline()
		file.close()

		output = calculate(string)
		filename = filename[:-4]
		file = open(f"{sys.argv[2]}/{filename}_n96249ty.txt", "w")
		file.write(output)
		file.close()
