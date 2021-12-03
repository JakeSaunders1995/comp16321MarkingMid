import sys
import os

args = sys.argv

def score_value(score_type):
    if (score_type == "t"):
        return 5
    elif (score_type == "c"):
        return 2
    elif (score_type == "d" or score_type == "p"):
        return 3
    else:
        print("invalid score type")
    return 0

def calc_score(scoring):

    t1_score = 0
    t2_score = 0

    for i in range(0, len(scoring)-1, 3):
        team = scoring[i:i+2]
        score_type = scoring[i+2]
        if (team == "T1"):
            t1_score += score_value(score_type)
        elif (team == "T2"):
            t2_score += score_value(score_type)
        else:
            print("ERROR : invalid team")

    result = str(t1_score) + ":" + str(t2_score)
    return result

input_dir = args[1]
output_dir = args[2]

for file_name in os.listdir(input_dir):
    input_file = open(os.path.join(input_dir, file_name), "r")
    output_file = open(os.path.join(output_dir,(file_name + "_y66466tl")), "w")
    scoring = input_file.read()
    result = calc_score(scoring)
    output_file.write(result)
