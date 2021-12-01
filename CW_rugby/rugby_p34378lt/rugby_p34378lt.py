import sys
import os
inFolder = sys.argv[1]
outFolder = sys.argv[2]

for file in os.listdir(inFolder):
    if file.endswith('.txt'):
        score_file = open(inFolder + '/' + file, 'rt')
        score_text = (score_file.read()).strip()


        T1_score = 0
        T2_score = 0

        scoring = {
            't': 5,
            'c': 2,
            'p': 3,
            'd': 3
        }

        current_team = 1
        for char in score_text:
            if char == '1':
                current_team = 1
            elif char == '2':
                current_team = 2
            elif char.islower():
                if current_team == 1:
                    T1_score += scoring[char]
                else:
                    T2_score += scoring[char]


        if T1_score > T2_score:
            winner = "T1"
        elif T1_score < T2_score:
            winner = "T2"
        else:
            winner = "draw"

        outputName = file[:-4] + "_p34378lt"
        try:
            new_file = open(outFolder + '/' + (outputName + '.txt'), 'x')
        except:
            new_file = open(outFolder + '/' + (outputName + '.txt'), 'w')

        new_file.write(str(T1_score) + ':' + str(T2_score))

        score_file.close()
        new_file.close()