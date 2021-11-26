import os, sys

t,c,p,d = 5,2,3,3
for filename in os.listdir(sys.argv[1]):
    with open(os.path.join(sys.argv[1], filename), 'r') as f:
        if filename.endswith(".txt"):
            scores = f.read().rstrip()
            team1 = 0
            team2 = 0
            n = 0
            while n < (len(scores)/3):
                n+=1
                if scores[3*n-2] == "1":
                    if scores[3*n-1] == "t":
                        team1 += 5
                    elif scores[3*n-1] == "c":
                        team1 += 2
                    elif scores[3*n-1] == "p":
                        team1 += 3
                    elif scores[3*n-1] == "d":
                        team1 += 3
                elif scores[3*n-2] == "2":
                    if scores[3*n-1] == "t":
                        team2 += 5
                    elif scores[3*n-1] == "c":
                        team2 += 2
                    elif scores[3*n-1] == "p":
                        team2 += 3
                    elif scores[3*n-1] == "d":
                        team2 += 3
            filename = filename[:-4]
            path = sys.argv[2]
            f = open(os.path.join(path, filename + "_e58690mu.txt"), 'w')
            f.write(f"{team1}:{team2}")
        else:
            continue
