import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

valuations = {
    "t": 5,
    "c": 2,
    "p": 3,
    "d": 3
}

def score_calc(path):
    input_text = open(path, "r").read()
    scorings = [input_text[i:i+3] for i in range(0, len(input_text), 3)]
    team1, team2 = 0, 0
    for scoring in scorings:
        if scoring[0:2] == "T1":
            team1 += valuations[scoring[2]]
        else:
            team2 += valuations[scoring[2]]
    return f"{team1}:{team2}"

def main():
    for dir, subdirs, files in os.walk(args.input_path):
        for file in files:
            result = score_calc(os.path.join(dir, file))
            output_path = os.path.join(args.output_path, os.path.splitext(file)[0] + "_x43615kc.txt")
            if not os.path.exists(args.output_path):
                os.makedirs(args.output_path)
            with open(output_path, "w") as file:
                file.write(result)



if __name__ == '__main__':
    main()