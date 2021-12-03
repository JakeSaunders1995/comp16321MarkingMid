import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("engWords", help="English words file path")
parser.add_argument("input", help="Input file path here")
parser.add_argument("output", help="Output file path here")
args = parser.parse_args()

f = open(args.engWords,"r")
wordList = f.read().split("\n")
f.close()
punc = [".","?","!",",",":",";","-","'","[","]","(",")","{","}","/",'"',"😊"]
number = ["0","1","2","3","4","5","6","7","8","9"]
for file in os.listdir(args.input):
    if file.endswith(".txt"):
        f = open(os.path.join(args.input, file),"r")
        data = f.read()
        f.close()

        up = 0
        pu = 0
        nu = 0
        deleting = []
        data=data.replace("...","😊")
        for i in range(len(data)):
            if data[i].isupper()==True:
                up += 1
            if data[i] in punc:
                pu += 1
            if data[i] in number:
                nu += 1

                
        data = data.lower()
        data = data.strip()
        for i in punc:
            data=data.replace(i,"")
        for i in number:
            data=data.replace(i,"")
        words = data.split(" ")
        bad = 0
        good = 0
        for z in words:
            if z not in wordList and z != "":
                bad += 1
            if z in wordList:
                good += 1
        length = good + bad
        lines = ["j14769hd\n",
                 "Formatting ###################\n",
                 "Number of upper case words changed: "+str(up)+"\n",
                 "Number of punctuations removed: "+str(pu)+"\n",
                 "Number of numbers removed: "+str(nu)+"\n",
                 "Spellchecking ###################\n",
                 "Number of words: "+str(length)+"\n",
                 "Number of correct words: "+str(good)+"\n",
                 "Number of incorrect words: "+str(bad)+"\n"
            ]
        output = "".join(lines)

        name = file.split(".")[0]
        name = name + "_j14769hd.txt"
        if not os.path.exists(args.output):
            os.mkdir(args.output)
        f = open(os.path.join(args.output,name),"w+")
        f.write(output)
        f.close()
        print(words)
