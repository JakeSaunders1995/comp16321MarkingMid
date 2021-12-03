import sys

with open(sys.argv[1], 'r') as f:
    results = f.read()

team_1=0
team_2=0
points=0
team=0

for n in results:
    if n == "T":
        points=0
    if n == "1":
        team=1
    elif n == "2":
        team=2
    elif n == "t":
        points=5
    elif n == "c":
        points=2
    elif n == "p":
        points=3
    elif n == "d":
        points=3
    if team==1:
        team_1+=points
    elif team==2:
        team_2+=points

with open(sys.argv[2], 'w') as f:
    f.write(str(team_1)+":"+str(team_2))

