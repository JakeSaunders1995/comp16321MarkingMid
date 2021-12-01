import os
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="enter input file")
    parser.add_argument("out_file", help="enter output file")
args = parser.parse_args()
input_file = args.in_file
for k in os.listdir(input_file):
    txt_position = k.find('.txt')
    input_file_name = k[0:txt_position]
    file = open(f'{args.in_file}/{k}','r')
    theScore = []
    for line in file:
        line = line.rstrip()
        theScore.append(line)
    score_input = theScore[0]
    score_T1 = 0
    score_T2 = 0
    length_of_score = len(score_input)
    for r in range(1, length_of_score, 3):
        team = score_input[r]
        if team == '1':
            if score_input[r + 1] == 't':
                score_T1 += 5
            elif score_input[r + 1] == 'c':
                score_T1 += 2
            elif score_input[r + 1] == 'p':
                score_T1 += 3
            elif score_input[r + 1] == 'd':
                score_T1 += 3
        elif team == '2':
            if score_input[r + 1] == 't':
                score_T2 += 5
            elif score_input[r + 1] == 'c':
                score_T2 += 2
            elif score_input[r + 1] == 'p':
                score_T2 += 3
            elif score_input[r + 1] == 'd':
                score_T2 += 3
    print(f'{score_T1}:{score_T2}')
    if score_T1 > score_T2:
        print('congratulations! Team 1 won')
    elif score_T1 < score_T2:
        print('congratulations! Team 2 won')
    else:
        print('it was a draw between the teams')
    print("----------------------------\n")
    line = [f'{score_T1}:{score_T2}']
    with open(os.path.join(args.out_file, f'{input_file_name}_m55182va.txt'), 'w') as f:
        f.writelines(line)
