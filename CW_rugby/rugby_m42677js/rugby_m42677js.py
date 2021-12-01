import argparse

parser = argparse.ArgumentParser(description="Who win? Team 1 or Team2?")
parser.add_argument('input', type=argparse.FileType('r'), help="input scoring file")
parser.add_argument('o', type=argparse.FileType('w'), help="output the score to a file")
args = parser.parse_args()

score = args.input.read()

i = 0
t1 = 0
t2 = 0


while (i < len(score)):
	string = score[i]
	i += 1
	if (string == "1" ):
		if (score[i] == "t"):
			t1 += 5
		elif (score[i] == "c"):
			t1 += 2
		elif (score[i] == "p"):
			t1 += 3
		elif(score[i] == "d"):
			t1 += 3
		else:
			continue


	elif (string == "2"):
		if (score[i] == "t"):
			t2 += 5
		elif (score[i] == "c"):
			t2 += 2
		elif (score[i] == "p"):
			t2 += 3
		elif(score[i] == "d"):
			t2 += 3
		else:
			continue



	else:
		continue


print("t1 score " + str(t1))
print("t2 score " + str(t2))


if (t1 > t2):
	print("Team 1 win")
elif (t1 == t2):
	print("Team 1 and Team 2 draw")
else:
	print("Team 2 win")

file = args.o.write("%d:%d" %(t1, t2))