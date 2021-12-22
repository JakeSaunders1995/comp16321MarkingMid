#Please let me know if the folder input and output could be done easier and shorter than this
import argparse, glob, os
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument('folderin', help = "input folderpath")
parser.add_argument('folderout', help = "output folderpath")
args = parser.parse_args()
pathin = args.folderin
pathout = args.folderout
for filename in glob.glob(os.path.join(pathin, '*.txt')):
   with open(os.path.join(os.getcwd(), filename)) as f:
        namein = Path(filename).stem
        nameout = namein + "_j80841pg.txt"
        completeName = os.path.join(pathout, nameout)
        filein = open(filename)
        fileout = open(completeName, 'w')
        t1 = 0
        t2 = 0
        text = list(filein.read())

        for i in range(2, len(text), 3):
            if text[i] == 't':
                if text[i-1] == '1':
                    t1 += 5
                else:
                    t2 += 5
            elif text[i] == 'c':
                if text[i-1] == '1':
                    t1 += 2
                else:
                    t2 += 2
            elif text[i] == 'p' or text[i] == 'd':
                if text[i-1] == '1':
                    t1 += 3
                else:
                    t2 += 3
        fileout.write(str(t1) + ':' + str(t2))
        filein.close()
        fileout.close()
