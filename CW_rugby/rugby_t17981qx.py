import argparse
import os.path

parser = argparse.ArgumentParser(description="Rugby score calculator")
parser.add_argument("input_filepath", help="input file path")
parser.add_argument("output_filepath", help="output file path")
args = parser.parse_args()

args.input_filepath = os.path.abspath(args.input_filepath)
args.output_filepath = os.path.abspath(args.output_filepath)

for file_name in os.listdir(args.input_filepath):
    os.chdir(args.input_filepath)
    with open(os.path.join(os.getcwd(), file_name), 'r') as f:

        score = open((os.path.join(os.getcwd(), file_name)), "r")
        scorelist = []
        for i in score:
            scorelist += i

        T1score = 0
        T2score = 0

        i = 0
        while i < len(scorelist):
            if scorelist[i] == "1":
                if scorelist[i + 1] == "t":
                    T1score += 5
                elif scorelist[i + 1] == "c":
                    T1score += 2
                elif scorelist[i + 1] == "p":
                    T1score += 3
                else:
                    T1score += 3
            elif scorelist[i] == "2":
                if scorelist[i + 1] == "t":
                    T2score += 5
                elif scorelist[i + 1] == "c":
                    T2score += 2
                elif scorelist[i + 1] == "p":
                    T2score += 3
                else:
                    T2score += 3
            i += 1

        if T1score > T2score:
            print("Team 1 wins!")
        elif T1score < T2score:
            print("Team 2 wins!")
        else:
            print("Draw!")


    os.chdir(args.output_filepath)
    file_name = file_name[:-4] + "_t17981qx.txt"
    with open(file_name, 'w') as d:
        d.write(str(T1score) + ":"+str(T2score))






















