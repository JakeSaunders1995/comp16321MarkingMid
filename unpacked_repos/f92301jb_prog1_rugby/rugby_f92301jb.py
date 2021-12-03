import sys
import os

path = sys.argv[1]
for file in os.listdir(path):
    file_path = os.path.join(os.getcwd(), path) + "/" + file
    if os.path.isfile(file_path):

        scoreboard_file = open(file_path, 'r')
        scoreboard = (scoreboard_file.read())
        scoreboard_file.close()

        team1_total = 0
        team2_total = 0

        scoreboard_array = []
        for character in scoreboard:
            scoreboard_array.append(character)

        for i in range(2,len(scoreboard_array),3):
            if (scoreboard_array[i] == "t"):
                score_type_value = 5
            elif (scoreboard_array[i] == "c"):
                score_type_value = 2
            elif (scoreboard_array[i] == "p" or scoreboard_array[i] == "d"):
                score_type_value = 3
            else:
                pass

            if scoreboard_array[i-1] == "1":
                team1_total += score_type_value
            elif scoreboard_array[i-1] == "2":
                team2_total += score_type_value
            else:
                pass

        final_scores = (str(team1_total)+":"+str(team2_total))

        output_file_name = os.path.join(os.getcwd(), sys.argv[2]) + "/" + file[:-4] + "_f92301jb.txt"
        output_file = open(output_file_name, "w")
        output_file.write(final_scores)
        output_file.close()
