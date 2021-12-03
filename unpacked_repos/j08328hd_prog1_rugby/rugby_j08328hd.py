import sys, os

count =  0

inPath = sys.argv[1]
outPath = sys.argv[2]

inFiles = os.listdir(inPath)
inFiles.sort()

#Create for loop to loop through all the files in the folder.

for file in inFiles:
    count += 1
    t1 = 0
    t2 = 0
    fIn = open(inPath + "/" + file, "r")
    fOut = open(outPath + "/test_file"+str(count)+"_j08328hd.txt", "w")
    data = fIn.read()
    dataAr = data.split('T')
    dataAr.remove('')

    for i in dataAr:
        score = 0
        if i[1] == 't':
            score = 5
        elif i[1] == 'c':
            score = 2
        elif i[1] == 'p' or i[1] == 'd':
            score = 3
        else:
            score = 0
        if i[0] == '1':
            t1 = t1 + score
        elif i[0] == '2':
            t2 = t2 + score
        else:
            pass

    if t1 > t2:
        print('Team 1 wins!')
    elif t1 < t2:
        print('Team 2 wins!')
    else:
        print('The game was a draw.')

    final = str(t1)+ ':'+ str(t2)
    fOut.write(final)
    fOut.close()