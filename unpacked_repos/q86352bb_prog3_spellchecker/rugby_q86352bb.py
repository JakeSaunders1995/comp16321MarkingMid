import sys
import os
filles =[]
filles = os.listdir(str(sys.argv[1])) # Get all test files and put in list
for p in filles:
    if not p.startswith('.'):       #Ignores the hidden files
        fpath1 = str(sys.argv[1])
        fullname1 = os.path.join(fpath1,p)      #creates filepath for inputs
        fi1le = open(fullname1, encoding="utf8", errors='ignore')
        fpath = str(sys.argv[2])
        p = str(p)
        pos = int(p.find(".txt"))          
        fname = p[:pos] + "_q86352bb.txt"
        fullname = os.path.join(fpath,fname)       #creates the filename for the outouts 
        f = open(fullname, "w")
        y=0
        team2=0
        team1 = 0
        z = 2
        for x in fi1le:
            score = str(x)
            length = len(x)
            while y <= length-3:
                if score[y:z] == "T2":
                    if score[z:z+1] == "t":
                        team2 += 5
                    elif score[z:z+1] =="c":
                        team2 += 2
                    elif score[z:z+1] =="p":
                        team2 += 3
                    elif score[z:z+1] =="d":
                        team2 += 3
                if score[y:z] == "T1":
                    if score[z:z+1] == "t":
                        team1 += 5
                    elif score[z:z+1] =="c":
                        team1 += 2
                    elif score[z:z+1] =="p":
                        team1 += 3
                    elif score[z:z+1] =="d":
                        team1 += 3
                y+=3
                z+=3
        fi1le.close()
        if team1 > team2:
            winner = "team1"
        elif team1 < team2:
            winner ="team2"
        else: 
            winner= "draw"
        f.write(str(team1)+":"+str(team2))

                

            






