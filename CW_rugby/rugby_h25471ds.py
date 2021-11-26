import os, argparse, re


input_folder_path = ""
output_folder_path = ""
scores = {"t":5, "c":2, "p":3, "d":3}

def cmdline(): # To get arguments from command line
    global input_folder_path, output_folder_path
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', type=str)
    parser.add_argument('output_path', type=str)
    args = parser.parse_args()

    input_folder_path = args.input_path
    output_folder_path = args.output_path


def fileextraction(arg):
    files = os.listdir(arg)
    for file in files:
        if file.endswith(".txt"): continue
        else: files.remove(file)
    return files


def inputfile(arg): # read the input file and store it in a variable
    with open(os.path.join(input_folder_path,arg), "r+") as file:
        x = file.readline()
        return x


def split_data(arg): # get the team scores
    data_list = re.split("([tcpd])", arg)
    return data_list

def outputfile(arg1, arg2): # store the output in the output file
    T1, T2 = 0, 0
    for i in range(len(arg1)):
        if arg1[i] == "T1":
            T1 += scores[arg1[i+1]]
        elif arg1[i] == "T2":
            T2 += scores[arg1[i+1]]
        else: continue
    if os.path.exists(output_folder_path): 
        pass
    else: os.makedirs(output_folder_path)
    with open(os.path.join(output_folder_path,arg2),"w+") as file:
        file.write(f"{T1}:{T2}")


def main():
    cmdline()
    input_files = fileextraction(input_folder_path)
    for testfile in input_files:
        teamscores = inputfile(testfile)
        data = split_data(teamscores)
        outputfilename = re.split("[.]",testfile)[0] + "_h25471ds.txt"
        outputfile(data, outputfilename)

main()

