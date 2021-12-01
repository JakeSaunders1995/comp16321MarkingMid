import sys, os
inputpath = sys.argv[1]
if inputpath.endswith("/"):
    pass
else:
    inputpath += "/"
outputpath = sys.argv[2]  
if outputpath.endswith("/"):
    pass
else:
    outputpath += "/"
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
for filepath in os.listdir(inputpath):
    if filepath.endswith(".txt"):
        fileinput = os.path.join(inputpath, filepath)
        file = open(fileinput)
        line = file.read()
        file.close()
        Team1, Team2 = 0, 0
        splitintothree = [line[x: x + 3] for x in range(0, len(line), 3)]
        for x in range(len(splitintothree)):
            if "T1" in splitintothree[x]:
                if "t" in splitintothree[x]: Team1 += 5
                if "c" in splitintothree[x]: Team1 += 2
                if "p" in splitintothree[x]: Team1 += 3
                if "d" in splitintothree[x]: Team1 += 3
            elif "T2" in splitintothree[x]:
                if "t" in splitintothree[x]: Team2 += 5
                if "c" in splitintothree[x]: Team2 += 2
                if "p" in splitintothree[x]: Team2 += 3
                if "d" in splitintothree[x]: Team2 += 3
        if Team1 > Team2:
            winner = "The Winner Is Team 1"
        elif Team2 > Team1:
            winner = "The Winner Is Team 2"
        else:
            winner = "The Game Is A Draw"
        filepath = filepath.replace(".txt","_m42552rh.txt")
        fileoutput = os.path.join(outputpath, filepath)  
        outputfile = open(fileoutput, "w")
        outputfile.write(str(Team1) + ":" + str(Team2))
        outputfile.close()
        