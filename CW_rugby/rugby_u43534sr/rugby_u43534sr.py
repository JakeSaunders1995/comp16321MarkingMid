''''

• t = 5 points (Try)
• c = 2 points (Goal kick)
• p = 3 points (Penalty)
• d = 3 points (Drop goal)


''''
import sys

InputFile = sys.argv[1]
OutputFile = sys.argv[2]

Team1Total = 0
Team2Total = 0

with open(InputFile, 'r') as f:
    while True:
        team_score = f.read(3)
        if not team_score:
            break
        elif team_score == T1t:
            Team1Total += 5
        elif team_score == T1c:
            Team1Total += 2
        elif team_score == T1p:
            Team1Total += 3
        elif team_score == T1d:
            Team1Total += 3
        elif team_score == T2t:
            Team2Total += 5
        elif team_score == T2c:
            Team2Total += 2
        elif team_score == T2p:
            Team2Total += 3
        elif team_score == T2d:
            Team2Total += 3

Team1score = str(Team1Total)
Team2score = str(Team2Total)



with open(OutputFile, 'w') as x:
    x.write(Team1score + ':' + Team2score)





