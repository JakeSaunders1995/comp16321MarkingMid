import argparse, os, re

parser = argparse.ArgumentParser()
parser.add_argument('inputpath', type=str, help= 'paste path to input files')
parser.add_argument('outputpath', type=str, help= 'paste path to output files')

originalpath = os.getcwd()
args = parser.parse_args()
path = args.inputpath
output_path = args.outputpath
os.chdir(args.inputpath)
cwd = os.getcwd()

# storing file names into variables
input_file_names = os.listdir()

txt = '.txt'
counter = 0
for n in range(len(input_file_names)):
    if re.search(txt, input_file_names[n]):
        counter += 1

for n in range(len(input_file_names)):
    input_file_names[n] = re.split(r'\.txt', input_file_names[n])

# reads file
def read_input(file_path):
    global input_variable
    with open(file_path, 'r') as f:
        input_variable = str(f.read())
def actual_program(input_01):
    global output
    sets_of_scores = int(len(input_01) / 3)
    n = 1
    sumT1 = 0
    sumT2 = 0
    while n <= sets_of_scores:
        team = input_01[3*n - 2]
        if team == "1":
            scoreT1 = input_01[3*n - 1]
            if scoreT1 == "t":
                score = 5
            elif scoreT1 == "c":
                score = 2
            elif scoreT1 == "p":
                score = 3
            elif scoreT1 == "d":
                score = 3
            sumT1 = sumT1 + score
        elif team == "2":
            scoreT2 = input_01[3*n - 1]
            if scoreT2 == "t":
                score = 5
            elif scoreT2 == "c":
                score = 2
            elif scoreT2 == "p":
                score = 3
            elif scoreT2 == "d":
                score = 3
            sumT2 = sumT2 + score  
        n += 1       

    # if sumT1 == sumT2:
    #     print("Draw")
    # elif sumT1 > sumT2:
    #     print("T1 wins")
    # elif sumT2 > sumT1:
    #     print("T2 wins")

    output = str(sumT1) + ":" + str(sumT2)

# iterate through all file
counter = 0
for file in os.listdir():
    # Check whether file is in text format or not
    if path.startswith(".") or file.endswith(".txt"):
        file_path = f"{cwd}/{file}"

        # call read text file function
        read_input(file_path)
        actual_program(input_variable)


        # to make output available with ./output
        if output_path.startswith("."):
            output_path_edited = output_path[2:]
            output_path_dir = f"{originalpath}/{output_path_edited}"
            os.chdir(output_path_dir)
        else:
            os.chdir(args.outputpath)

        for n in range(len(input_file_names[counter])):
            if input_file_names[counter][n] != '':
                file_name = input_file_names[counter][n]

        counter += 1

        with open("{}_p55643na.txt".format(file_name), "w") as f:
            f.write("{}".format(output))

    else:
        break