import os
import sys

scoremap = {
    "t": 5,
    "c": 2,
    "p": 3,
    "d": 3
}

# read params from the terminal
args = sys.argv
if len(args) != 3:
    print("error")
else:
    inputdirectorypath = args[1]
    outputdirectorypath = args[2]
    if not os.path.exists(outputdirectorypath):
        os.mkdir(outputdirectorypath)
    for filename in os.listdir(inputdirectorypath):
        inputfilepath = inputdirectorypath + "/" + filename
        t1 = 0
        t2 = 0

        file = open(inputfilepath, 'r')
        line = file.read()
        for i in range(0, len(line), 3):
            data = line[i:i+3]
            if data[1] == "1":
                t1 += scoremap[data[2]]
            else:
                t2 += scoremap[data[2]]
        file.close()

        outputfilename = outputdirectorypath + '/' + filename.split(".")[0] + "_p44797jb.txt"
        file = open(outputfilename, "w")
        file.write(str(t1) + ":" + str(t2))
        file.close()
