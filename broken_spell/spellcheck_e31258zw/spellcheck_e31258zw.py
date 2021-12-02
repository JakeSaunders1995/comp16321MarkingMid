# Program 3 - Spellchecker - e31258zw - Ziyi Wang
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("Eng_words")
parser.add_argument("folder_in")
parser.add_argument("folder_out")
args = parser.parse_args()

files_arr = []      # store the files name in an array

# punctuation list
#                       dash contain: en dash (–) and the em dash (—)
punc_arr = ['.','?','!',',',':',';','-','–','—','[',']','{','}','(',')',"'",'"','...']

def file_name(folder):
    """ 
    function to get the files from the input folder from the command 
    :folder: the folder where the file needs to be extracted
    """
    global files_arr
    for files in os.walk(folder):
        files_arr = files[2]

def check_correct(arr):
    """ 
    function to check the correct words 
    :arr: a list of words need to check 
    """ 
    global correct_w, incorrect_w
    # open the file in a read mode
    Eng = open(args.Eng_words,"r")
    for line in Eng:
        for i in range(len(arr)): 
            # get rid of any '\n' and space in the 'line', and compare the words
            if (arr[i] == line.strip()):
                correct_w += 1
    Eng.close()   

# main program ----------------------------------------------------------------

# extract files and store in the array 'files_arr' 
file_name(args.folder_in)

# no need to check
# check if the output folder exist -> if not, create
# if not os.path.exists(args.folder_out):
#     os.makedirs(args.folder_out)

for item in files_arr:
    # initialization
    # the string write into the output file
    write_str = "e31258zw\nFormatting ###################\n"
    number_rm = 0       # number of numbers removed
    punctuation_rm = 0  # number of punctuation's removed
    upper_trans = 0     # number of upper case words transformed
    correct_w = 0       # number of correct words
    incorrect_w = 0     # incorrect words

    word_arr = []   # store the words extracted in the text

    file_in_path = args.folder_in + "/" + item
    file_out_path = args.folder_out + "/" + item[:-4] + "_e31258zw.txt"

    # open the file in a read mode
    file_r = open(file_in_path,"r")
    str_in = file_r.read()
    file_r.close()

    count = 0       # index of the string -> extract character
    cur_words = ""  # store the current words
    while (count < len(str_in)):
        char_in = str_in[count]

        if char_in in "1234567890":     # numbers
            number_rm += 1
            count += 1
        elif char_in in punc_arr:       # punctuation
            if (char_in == '.'):
                # chrck if it is '...'
                if (count +2 < len(str_in) and str_in[count + 1] == '.' and str_in[count + 2] == '.'):
                    punctuation_rm += 1
                    count += 3
                else:
                    punctuation_rm += 1
                    count += 1
            else:
                punctuation_rm += 1
                count += 1
        elif (ord(char_in) > 64 and ord(char_in) < 91):     # A -> 65; Z -> 90 (uppercase)
            upper_trans += 1
            cur_words = cur_words + chr(ord(char_in) + 32)
            count += 1
        elif (ord(char_in) > 96 and ord(char_in) < 123):    # a -> 97; z -> 122
            cur_words = cur_words + char_in
            count += 1
        elif (char_in == " " or char_in == '\n'):       # space and newline
            if (cur_words != ""):
                word_arr.append(cur_words)
                cur_words = ""
            count += 1
        # else:       # anything else will be considered as punctuation
        #     punctuation_rm += 1
        #     count += 1

    # do remember to add the last one if there is no space or '\n' at the end
    if (cur_words != ""):
        word_arr.append(cur_words)

    check_correct(word_arr)
    incorrect_w = len(word_arr) - correct_w

    write_str = write_str + "Number of upper case letters chenged: " + str(upper_trans) + '\n'
    write_str = write_str + "Number of punctuations removed: " + str(punctuation_rm) + '\n'
    write_str = write_str + "Number of numbers removed: " + str(number_rm) + '\n'
    write_str = write_str + "Spellchecking ###################\n"
    write_str = write_str + "Number of words: " + str(len(word_arr)) + '\n'
    write_str = write_str + "Number of correct words: " + str(correct_w) + '\n'
    write_str = write_str + "Number of incorrect words: " + str(incorrect_w) + '\n'

    # open the file for writing, create if it doesn't exist
    file_w = open(file_out_path,"w")

    file_w.write(write_str)
    file_w.close()

