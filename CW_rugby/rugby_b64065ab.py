import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('input_directory')
parser.add_argument('output_directory')
args = parser.parse_args()

input_directory = args.input_directory
output_directory = args.output_directory

i = 1
for filename in os.scandir(input_directory):
    if filename.is_file():
        f = open(filename.path)
        scores = f.read()

        t1Scores=0
        t2Scores = 0
        
        lst = scores.split("T")
        lst.pop(0)

        points = {"t": 5, "c": 2, "p": 3, "d": 3}

        for ele in lst:
            if ele[0] == "1":
                t1Scores += points[ele[1]]
            else:
                t2Scores += points[ele[1]]

        finalScores = str(t1Scores) + ":" + str(t2Scores)
        cwd = os.getcwd()
        os.chdir(output_directory)
        outputname  = "test_file" + str(i) + "_b64065ab.txt"
        output = open(outputname, "w")
        output.write(finalScores)
        output.close()
        i += 1
        os.chdir(cwd)
        cwd = ""