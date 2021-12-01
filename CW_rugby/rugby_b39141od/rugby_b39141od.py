import sys
import os
files = os.listdir(sys.argv[1])

for file in files:
    f = open(os.path.join(sys.argv[1], file))
    events = f.read()
    f.close()
    events = [events[i:i+3] for i in range(0,len(events),3)]

    t1score = 0
    t2score = 0

    for event in events:
        #calculate no of points to be awarded
        award = 0
        if event[2] == "t":
            award = 5
        elif event[2] == "c":
            award = 2
        elif event[2] == "p":
            award = 3
        elif event[2] == "d":
            award = 3

        #add award to according team
        if event[1] == "1":
            t1score += award
        else:
            t2score += award
    if t1score > t2score:
        print("Team 1 Wins")
    elif t1score == t2score:
        print("Draw")
    else:
        print("Team 2 Wins")
    o = open(os.path.join(sys.argv[2], file[:-4]+"_b39141od.txt"),'w')
    o.write(str(t1score)+":"+str(t2score))
    o.close()
