import argparse
import re
import os

def score_add(element):
    score = 0
    result_t = re.search(r"t$", element)
    result_c = re.search(r"c$", element)
    result_p = re.search(r"p$", element)
    result_d = re.search(r"d$", element)
    if result_t:
        score += 5
    elif result_c:
        score += 2
    elif result_p:
        score += 3
    elif result_d:
        score += 3
    return score

parser = argparse.ArgumentParser()
parser.add_argument("inputfilepath", help="The input file path")
parser.add_argument("outputfilepath", help="The output file path")
args = parser.parse_args()

inputdirectory = args.inputfilepath
outputdirectory = args.outputfilepath

for filename in os.listdir(inputdirectory):
    with open(os.path.join(inputdirectory, filename)) as inputfile:
        score_string = inputfile.read()
        score_string_split = score_string.split("T")

    t1_score = 0
    t2_score = 0

    for element in score_string_split:
        result_1 = re.match("^1", element)
        result_2 = re.match("^2", element)
        if result_1:
            score_add(element)
            t1_score += score_add(element)
        elif result_2:
            score = score_add(element)
            t2_score += score

    filename_split = filename.split(".")
    filename_split.insert(1, "_j78134fm.")
    filename_otpt = "".join(filename_split)
    filename_output = os.path.join(outputdirectory, filename_otpt)

    with open(filename_output, "w") as outputfile:
        outputfile.write(str(t1_score) + ":" + str(t2_score))
