import argparse, os

myparser = argparse.ArgumentParser(description='Rugby score calculator')

myparser.add_argument('input_file_path')
myparser.add_argument('output_file_path')

args = myparser.parse_args()

input_path = args.input_file_path
output_path = args.output_file_path

for file in os.listdir(input_path):
    with open(os.path.join(input_path, file), 'r') as f:
        scoreline = f.read()
        filename = os.path.basename(f.name)[:-4]

    event_count = len(scoreline)//3

    t1score = 0
    t2score = 0
    scoring_team = ""

    for _ in range(event_count):
        event, scoreline = scoreline[:3], scoreline[3:]
        team, type = event[:2], event[2:]
        if team == "T1":
            if type == 't':
                t1score += 5
            elif type == 'c':
                t1score += 2
            elif type == 'p':
                t1score += 3
            elif type == 'd':
                t1score += 3
        elif team == "T2":
            if type == 't':
                t2score += 5
            elif type == 'c':
                t2score += 2
            elif type == 'p':
                t2score += 3
            elif type == 'd':
                t2score += 3

    output_filename = filename + "_h06023jc.txt"

    with open(os.path.join(output_path, output_filename),'w',encoding='utf-8') as f:
        f.write(str(t1score) + ':' + str(t2score))