import random
import sys
import os



def init():
    team1score = 0
    team2score = 0
    n = 0
    input_rugby = sys.argv[1]
    output_rugby = sys.argv[2]
    text_scores = []
    input_folder_amount = 0
    to_be_returned = [team1score, team2score, n, input_rugby, output_rugby, text_scores, input_folder_amount]
    return to_be_returned

def file_reading(inp):
    for score_sheet in sorted(os.listdir(inp[3])):
        inp[6] += 1
        with open(os.path.join(inp[3], score_sheet), 'r') as f:
            score_sheet_to_string = f.read().rstrip()
            inp[5].append(score_sheet_to_string)

def scoring(inp):
    currentfilenumber = 0
    for string in inp[5]:
        currentfilenumber += 1
        inp[0] = 0
        inp[1] = 0
        inp[2] = 0
        for letter in string:
            if letter == "1":
                if string[inp[2] + 1] == "t":
                    inp[0] += 5
                elif string[inp[2] + 1] == "c":
                    inp[0] += 2
                elif string[inp[2] + 1] == "p":
                    inp[0] += 3
                elif string[inp[2] + 1] == "d":
                    inp[0] += 3
            elif letter == "2":
                if string[inp[2] + 1] == "t":
                    inp[1] += 5
                elif string[inp[2] + 1] == "c":
                    inp[1] += 2
                elif string[inp[2] + 1] == "p":
                    inp[1] += 3
                elif string[inp[2] + 1] == "d":
                    inp[1] += 3
            inp[2] += 1
        outputs(inp, currentfilenumber)




def outputs(inp, currentfilenumber):
    Rugby_Score = "Rugby_Score" + str(currentfilenumber) + "_c70846fu"
    output = open(inp[4]+"/"+Rugby_Score+".txt", "w+")
    match_score = (str(inp[0]) + ":" + str(inp[1]))
    output.write(match_score)



#MAIN
x = init()
file_reading(x)
scoring(x)
