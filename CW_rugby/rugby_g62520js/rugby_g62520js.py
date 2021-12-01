
import argparse
import os

parser = argparse.ArgumentParser(description='Input and Output files')
parser.add_argument('input', type=str, help='Input file')
parser.add_argument('output', type=str, help='Output file')
args = parser.parse_args()

infile = args.input
outfile = args.output


score1 = 0
score2 = 0



for x in os.listdir(infile):

    f = os.path.join(infile, x)
    dir_path = os.path.dirname(f)
    read_scores = open(f, "r")
    results = read_scores.readline()


    score1 = 0
    score2 = 0

    for i in range(len(results) ):

        if i % 3 == 2:
            letter = results[i]
            number = results[i - 1]
            if number == "1":
                if letter == "t":
                    score1 += 5
                elif letter == "c":
                    score1 += 2
                elif letter == "p":
                    score1 += 3
                elif letter == "d":
                    score1 += 3
                else:
                    print("SOMETHING WENT WRONG")


            elif number == "2":
                if letter == "t":
                    score2 += 5
                elif letter == "c":
                    score2 += 2
                elif letter == "p":
                    score2 += 3
                elif letter == "d":
                    score2 += 3
                else:
                    print("SOMETHING WENT WRONG")








    if outfile[-1] == "/":
        out_name = outfile + x.split(".txt")[0] + "_g62520js.txt"
        output_file = out_name
        directory = os.path.dirname(outfile)
    else:
        out_name = outfile + "/" + x.split(".txt")[0] + "_g62520js.txt"
        output_file = out_name
        directory = os.path.dirname(output_file)
        #print(directory)


    if not os.path.exists(directory):
        os.makedirs(directory)

    winner = ""
    if score1 > score2:
        winner = "Winner is Team 1"
        #print(score1,score2)
    elif score1 < score2:
        winner = "Winner is Team 2"
        #print(score1,score2)
    elif score1 == score2:
        winner = "It is a tie"
        #print(score1,score2)

    final_scores = open(output_file, "w")
    final_scores.write(str(score1)+":"+str(score2))
    final_scores.close()
