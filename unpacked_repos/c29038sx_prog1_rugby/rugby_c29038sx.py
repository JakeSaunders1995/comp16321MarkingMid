import argparse
import os

parser = argparse.ArgumentParser(description = "calculate the score")
parser.add_argument("input", type = str, help = "give me the path of input folder")
parser.add_argument("output", type = str, help = "give me the path of output folder")
args = parser.parse_args()

def checkdir(path):
    if os.path.isdir(path):
        return
    else:
        os.mkdir(path)
    return

def nameGenerater(path):
    return os.path.splitext(os.path.basename(path))[0] + "_c29038sx.txt"

def fileFilter(fileList):
    for inx, val in enumerate(fileList):
        if os.path.splitext(val)[1] != ".txt":
            del fileList[inx]

checkdir(args.output)

fileLs = os.listdir(args.input)
fileFilter(fileLs)
for i in fileLs:
    t1 = 0
    t2 = 0
    
    inputPath = os.path.join(args.input, i)
    outputPath = os.path.join(args.output, nameGenerater(inputPath))
    f = open(inputPath)
    #f = open("/Users/jonoboru/Desktop/CodeLocal/Example_inputs_program1/test_file1.txt")
    score = f.read()
    f.close()
    for inx, val in enumerate(score):
        if val == "1":
            #print(val, ": ", score[inx + 1])
            if score[inx + 1] == "t":
                t1 += 5
            elif score[inx + 1] == "c":
                t1 += 2
            elif score[inx + 1] == "p":
                t1 += 3
            elif score[inx + 1] == "d":
                t1 += 3
            else:
                print("There is a invalid score in the input file")
                break
            
        if val == "2":
            #print(val, ": ", score[inx + 1])
            if score[inx + 1] == "t":
                t2 += 5
            elif score[inx + 1] == "c":
                t2 += 2
            elif score[inx + 1] == "p":
                t2 += 3
            elif score[inx + 1] == "d":
                t2 += 3
            else:
                print("There is a invalid score in the input file")
                break
            
    #f = open("score_c29038sx.txt", "w")
    f = open(outputPath, "w")
    f.write(str(t1) + ":" + str(t2))
    f.close()
