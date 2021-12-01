import sys
import os
infolder = sys.argv[1]
outfolder = sys.argv[2]

for filename in os.listdir(infolder):

    infile = open(infolder + "/" + filename, "r")

    line = infile.readline()

    t1 = 0
    t2 = 0

    for x in range(len(line)):
        if line[x] == '1':
            if line[x+1] == 't':
                t1 += 5
            elif line[x+1] == 'c':
                t1 += 2
            elif line[x+1] == 'p' or line[x+1] == 'd':
                t1 += 3

        if line[x] == '2':
            if line[x+1] == 't':
                t2 += 5
            elif line[x+1] == 'c':
                t2 += 2
            elif line[x+1] == 'p' or line[x+1] == 'd':
                t2 += 3

    infile.close()
    outstring = str(t1) + ":" + str(t2)

    outfile = open(outfolder + "/" + filename[:-4] + "_h32647nh.txt", "w")
    outfile.write(outstring)
    outfile.close()
