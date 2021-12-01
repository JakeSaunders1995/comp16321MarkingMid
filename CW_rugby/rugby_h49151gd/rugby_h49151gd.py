import sys, os

def count_team1():
    T1f = scores.count("T1t")
    T1c = scores.count("T1c")
    T1p = scores.count("T1p")
    T1d = scores.count("Tfd")
    global team1_score
    team1_score = T1f * 5 + T1c * 2 + T1p * 3 + T1d * 3

def count_team2():
            T2f = scores.count("T2t")
            T2c = scores.count("T2c")
            T2p = scores.count("T2p")
            T2d = scores.count("T2d")
            global team2_score
            team2_score = T2f * 5 + T2c * 2 + T2p * 3 + T2d * 3

input_folder = sys.argv[1]
output_folder = sys.argv[2]
files = os.listdir(input_folder)

i = 0
while (i < len(files)):
    f = open(os.path.join(input_folder, files[i]), "r")
    scores = f.read()
    count_team1()
    count_team2()
    print("Team1 scored " +str(team1_score) + " points")
    print("Team2 scored " +str(team2_score) + " points")
    scoreboard = str(team1_score) +":"+ str(team2_score)
    if (team1_score > team2_score):
        print("Team1 wins!")
    elif (team1_score < team2_score):
        print("Team2 wins!")
    else:
        print("It's a draw.")


    outputfile = "test_file" + str(i+1) + "_h49151gd.txt"
    with open(os.path.join(sys.argv[2] ,outputfile), "w") as file1:
        file1.write(scoreboard)
    
    i += 1


