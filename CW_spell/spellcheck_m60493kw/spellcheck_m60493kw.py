import argparse
import re
import os

username = "m60493kw"

parser = argparse.ArgumentParser()
parser.add_argument('english_words_path')
parser.add_argument('input_path')
parser.add_argument('output_path')
args = parser.parse_args()
a = os.listdir(args.input_path)
b = sorted(a)
for i in range(len(os.listdir(args.input_path))):
    with open(args.input_path + "/" + b[i], "r") as f:
        file = f.read()

    correct, numCnt = re.subn(r"\d", "", file)
    correct, pucCnt = re.subn(r"""[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~…]""", "", correct)

    upperCnt = 0
    for c in correct:
        if c.isupper():
            upperCnt += 1
    correct = correct.lower()

    words = re.split(r"\s+", correct.strip())


    with open(args.english_words_path, "r") as f:
        cwords = f.read().split("\n")

    correctCnt, incorrectCnt = 0, 0
    for w in words:
        if w in cwords:
            correctCnt += 1
        else:
            incorrectCnt += 1

    result = f"""{username}
Formatting ###################
Number of upper case letters changed: {upperCnt}
Number of punctuations removed: {pucCnt}
Number of numbers removed: {numCnt}
Spellchecking ###################
Number of words: {len(words)}
Number of correct words: {correctCnt}
Number of incorrect words: {incorrectCnt}
"""

    with open(args.output_path+"/test_file"+str(int(i)+1)+"_m60493kw.txt", "w") as f:
        f.write(result)

