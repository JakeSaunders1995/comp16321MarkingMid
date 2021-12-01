import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument('output')
args = parser.parse_args()
input_folder = args.input
output_folder = args.output
directory = input_folder
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        g = open(f, 'r')
        scorecard = g.read()
        scores = {'t': 5, 'p': 3, 'c': 2, 'd': 3}
        i = 0
        global player_1, player_2
        player_1 = 0
        player_2 = 0
        while i < len(scorecard):
            if(scorecard[i] in scores):
                if(scorecard[i-1] == '1'):
                    player_1 += scores[scorecard[i]]
                elif(scorecard[i-1] == '2'):
                    player_2 += scores[scorecard[i]]
            i += 1
        result = f'{player_1}:{player_2}'
        filename1 = filename[0:(len(filename)-4)]
        output_path = f'{output_folder}/{filename1}_y42270sg.txt'
        g = open(output_path, 'w')
        g.write(result)
        g.close()
