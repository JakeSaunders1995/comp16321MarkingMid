import sys
import os
import glob

pathIn = sys.argv[1]
pathOut = sys.argv[2]
dirIn = os.path.join(pathIn, '*.txt')

for i in glob.glob(dirIn):
    fIn = open(os.path.join(os.getcwd(), i), 'r')
    filename = os.path.splitext(os.path.basename(i))[0]
    match = str(fIn.read())

    scoreType = {1 : 't', 2 : 'c', 3 : 'p', 4 : 'd'}
    score = {1 : 5, 2 : 2, 3 : 3, 4 : 3}

    t1score = 0
    t2score = 0
    a = 0
    b = 3

    while (a <= len(match)-3 and b <= len(match)):
        event = match[a:b]
        if (event[1] == '1'):
            for x in scoreType:
                if (event[2] == scoreType[x]):
                    t1score += score[x]
        if (event[1] == '2'):
            for x in score:
                if (event[2] == scoreType[x]):
                    t2score += score[x]
        a += 3
        b += 3

    if os.path.exists(pathOut):
        newFile = filename + '_r22997aa.txt'
        dirOut = os.path.join(pathOut, newFile)
        fOut = open(dirOut, 'w')
        print(str(t1score) + ':' + str(t2score), file = fOut)
        fOut.close()
    else:
        os.makedirs(pathOut)
        newFile = filename + '_r22997aa.txt'
        dirOut = os.path.join(pathOut, newFile)
        fOut = open(dirOut, 'w')
        print(str(t1score) + ':' + str(t2score), file = fOut)
        fOut.close()
