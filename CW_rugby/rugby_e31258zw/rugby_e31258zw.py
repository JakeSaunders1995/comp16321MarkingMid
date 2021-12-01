# program 1 - rugby - e31258zw - Ziyi Wang
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("folder_in")
parser.add_argument("folder_out")
args = parser.parse_args()

# initialization
files_arr = []      # store the files name in an array

# store -> scoring types and quantity
score = {
    "t" : 5,    # Try
    "c" : 2,    # Goal Kick
    "p" : 3,    # Penalty
    "d" : 3     # Drop Goal
}

def file_name(folder):
    """ 
    function to get the files from the input folder from the command 
    :folder: the folder where the file needs to be extracted
    """
    global files_arr
    for files in os.walk(folder):
        files_arr = files[2]

# main program ----------------------------------------------------------------

# extract files and store in the array 'files_arr' 
file_name(args.folder_in)

# no need to check
# check if the output folder exist -> if not, create
# if not os.path.exists(args.folder_out):
#     os.makedirs(args.folder_out)

for item in files_arr:
    score_T1 = 0
    score_T2 = 0

    file_in_path = args.folder_in + "/" + item
    file_out_path = args.folder_out + "/" + item[:-4] + "_e31258zw.txt"

    # open the file in read mode -> read into a string
    file_r = open(file_in_path,"r")
    str_in = file_r.read()
    file_r.close()

    # loop  -> get character one by one
    for i in range(len(str_in)):
        if (str_in[i] == '1'):
            i += 1
            next_char = str_in[i]     # get the scoring types in the next character
            score_T1 = score_T1 + score[next_char]
        elif (str_in[i] == '2'):
            i += 1
            next_char = str_in[i]
            score_T2 = score_T2 + score[next_char]

    out_str = str(score_T1) + ":" + str(score_T2)

    # open the file for writing, create if it doesn't exist
    file_w = open(file_out_path,"w")

    file_w.write(out_str)
    file_w.close()

