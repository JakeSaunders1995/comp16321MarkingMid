import sys
import os

input_path = sys.argv[1]
output_path = sys.argv[2]

for file_name in os.listdir(input_path):
    with open(input_path + "/{}".format(file_name), "r") as f:
        character_read = f.read()
        f.close()

        t = 5
        c = 2
        p = 3
        d = 3

        t1_score = 0
        t2_score = 0

        for x in range(len(character_read)):
            if character_read[x : x + 2] == "1t":
                t1_score += 5
            elif character_read[x : x + 2] == "1c":
                t1_score += 2
            elif character_read[x : x + 2] == "1p":
                t1_score += 3
            elif character_read[x : x + 2] == "1d":
                t1_score += 3
            elif character_read[x : x + 2] == "2t":
                t2_score += 5
            elif character_read[x : x + 2] == "2c":
                t2_score += 2
            elif character_read[x : x + 2] == "2p":
                t2_score += 3
            elif character_read[x : x + 2] == "2d":
                t2_score += 3

        score_string = str(t1_score) + ":" + str(t2_score)
        
        if t1_score > t2_score:
            t1_win = "T1 is the winner."
        elif t1_score < t2_score:
            t2_win = "T2 is the winner."
        else:
            draw = "It is a draw."

        file_name = os.path.basename(input_path + "/{}".format(file_name))

        new_file_name = os.path.join(output_path, file_name.split(".")[0] + "_u95206ma.txt")
        rugby_scores = open(new_file_name, "w+")
        rugby_scores.write(score_string)
        rugby_scores.close()




    
