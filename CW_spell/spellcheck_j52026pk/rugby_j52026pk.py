import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

openf = os.listdir(args.input)
printf = os.listdir(args.output)

sCounter=0
while sCounter<len(openf):
    file=args.input+"/"+openf[sCounter]
    text=open(file, "r")

    word=""
    while True:
	    characters=text.read(1)
	    if not characters:
		    break
	    word += characters
    text.close()

    i=0
    T1=0
    T2=0
    while i<len(word):
        if word[i] == "1":
            points=word[i+1]
            if points == "t":
                T1+=5
            elif points=="c":
                T1+=2
            elif points=="p" or points=="d":
                T1+=3
            points=0
        elif word[i] == "2":
            points=word[i+1]
            if points == "t":
                T2+=5
            elif points=="c":
                T2+=2
            elif points=="p" or points=="d":
                T2+=3
            points=0
        i+=1

    score = str(T1) + ":" + str(T2)

    filename = openf[sCounter]
    filenameNew = filename[0:len(filename) - 4] + "_j52026pk.txt"

    printfile=open(filenameNew, "w")
    printfile.write(score)
    printfile.close()
    sCounter+=1
