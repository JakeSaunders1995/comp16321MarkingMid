import sys, os

def scorecalculator(type):
    if type == "t":
        return 5
    elif type == "c":
        return 2
    elif type == "p":
        return 3
    elif type == "d":
        return 3

inputfolder = sys.argv[1]
os.chdir(inputfolder)

for file in os.listdir():
        if file.endswith(".txt"):
            filepath = f"{inputfolder}/{file}"
            inputscores = open(filepath, "r")
            score = inputscores.read()
            inputscores.close()

            t1score=0
            t2score=0

            for i in range(2, len(score), 3):
                if (score[i-1] == "1"):
                    t1score += scorecalculator(score[i])
                elif (score[i-1] == "2"):
                    t2score += scorecalculator(score[i])
 
            outputfolder = sys.argv[2]
            outputresult = open(outputfolder+file[:-4]+"_p94302hm.txt", "w")
            outputresult.write(str(t1score) + ":" + str(t2score))
