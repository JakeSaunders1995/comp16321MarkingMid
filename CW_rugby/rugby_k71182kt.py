import argparse, os

def directory_path(string):
    if os.path.isdir(string):
        return string
    else:
        return str(string)

# input text file
python_file_location = os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument('inputpath', type=directory_path)
parser.add_argument('outputpath', type=directory_path)
args = parser.parse_args()
outputStringList = []
name_of_file_list = []
os.chdir(args.inputpath)
for file in os.listdir():
    if file.endswith(".txt"):
        with open(file, 'rb') as f:
            name_of_file = str(file)[0:len(str(file))-4] + "_k71182kt.txt"
            name_of_file_list.append(name_of_file)
            inputString = str(f.read())
            # calculate score for each team
            t1_score = 0
            t2_score = 0
            i = 0
            while i < len(inputString):
                if inputString[i] == "T":
                    if inputString[i+1] == "1":
                        if inputString[i+2] == "t":
                            t1_score = t1_score + 5
                        elif inputString[i+2] == "c":
                            t1_score = t1_score + 2
                        elif inputString[i+2] == "p":
                            t1_score = t1_score + 3
                        elif inputString[i+2] == "d":
                            t1_score = t1_score + 3
                    elif inputString[i+1] == "2":
                        if inputString[i+2] == "t":
                            t2_score = t2_score + 5
                        elif inputString[i+2] == "c":
                            t2_score = t2_score + 2
                        elif inputString[i+2] == "p":
                            t2_score = t2_score + 3
                        elif inputString[i+2] == "d":
                            t2_score = t2_score + 3
                i = i + 1

            # create score with ratio of scores T1:T2
            outputString = str(t1_score) + ":" + str(t2_score)
            outputStringList.append(outputString)

os.chdir(python_file_location)
directory = args.outputpath
if os.path.exists(directory):
    os.chdir(directory)
else:
    os.mkdir(directory)
    os.chdir(directory)

output_count = 0
for i in name_of_file_list:
    output_text_file = open(i, 'w')
    output_text_file.write(outputStringList[output_count])
    output_text_file.close()
    output_count = output_count + 1
