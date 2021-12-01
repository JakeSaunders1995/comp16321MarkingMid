import sys
import os


input_directory = sys.argv[1]
file_list = os.listdir(input_directory)

n=0
while n<= len(file_list)-1:

    test_file1= open(input_directory +"/" +file_list[n],"r")
    data = test_file1.read()
    Team1_Tries= data.count("T1t")
    Team1_GoalKick= data.count("T1c")
    Team1_Penalty=data.count("T1p")
    Team1_DropGoal=data.count("T1d")

    Team2_Tries= data.count("T2t")
    Team2_GoalKick= data.count("T2c")
    Team2_Penalty=data.count("T2p")
    Team2_DropGoal=data.count("T2d")


    Team1Score= (Team1_Tries*5)+(Team1_GoalKick*2)+(Team1_Penalty*3)+(Team1_DropGoal*3)
    Team2Score= (Team2_Tries*5)+(Team2_GoalKick*2)+(Team2_Penalty*3)+(Team2_DropGoal*3)

    Comparrison=(str(Team1Score)+":" + str(Team2Score))

    if Team1Score>Team2Score:
        print("Team 1 won")
    elif Team1Score<Team2Score:
        print("Team 2 won")
    else:
        print("It was a draw")

    test_file1.close()
    
    filename =str(file_list[n]).replace(".txt", "")
    output_directory =sys.argv[2]
    output_file =open(output_directory +"/"+filename+"a86442gs.txt", "w")
    output_file.write(Comparrison)
    output_file.close()

    n+=1


