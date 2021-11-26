import argparse
import re
import os

parser = argparse.ArgumentParser(description="Formatting Sentences")
parser.add_argument("englishfile", type=str, help="Input for sentences")
parser.add_argument("inputfile", type=str, help="Input for sentences")
parser.add_argument("formatfile", type=str, help="output for format")
args = parser.parse_args()

alphabet_lower = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b"
            ,"c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

punctuations= [".", ",", "!", "?", ":", ";", "(", ")", "[", "]", "\"", "'", "…", "-","{", "}", "—", "–"]
numbers = ["0", "1","2","3","4","5","6","7","8","9"]

formatfile= args.formatfile
inputfile = args.inputfile


for y in os.listdir(inputfile):
    store_directory = os.path.join(inputfile, y)
    file = open(store_directory, "r")

    englishwords = open(args.englishfile, "r")
    english_read = englishwords.read()
    english_split = re.split("\n", english_read)


    file_string = file.readline()


    filelength = len(file_string)


    new_string = ""

    punc_count = 0
    upper_count = 0
    num_count = 0

    for x in range(filelength):
        if file_string[x] in punctuations:
            punc_count +=1

    for x in range(filelength):
        if file_string[x] in alphabet_upper:
            upper_count +=1

    for x in range(filelength):
        if file_string[x] in numbers:
            num_count +=1

    for x in range(filelength):
        if file_string[x] in alphabet:
            if file_string[x] in alphabet_upper:
                lower_case = file_string[x].lower()
                new_string = new_string + lower_case
            else:
                new_string = new_string + file_string[x]
        elif file_string[x] is int :
            continue
        elif file_string[x] == " ":
                new_string = new_string + " "


    file_split = new_string.split()
    true_word = 0
    false_word = 0

    for x in range(len(file_split)):
        if file_split[x] in english_split:
            true_word +=1
        else:
            false_word +=1

    if formatfile[-1] != "/":
        outputfile = formatfile + "/" + y.split(".txt")[0] + "_p33067ay"
        directory_create = os.path.dirname(outputfile)

    else:
        outputfile = scoresfile + y.split(".txt")[0] + "_p33067ay"
        directory_create = os.path.dirname(outputfile)

    if not os.path.exists(formatfile):
        os.makedirs(formatfile)


    final = open(outputfile, "w")
    final.write("p33067ay" + "\nFormating:#########" + "\nNumber of uuper case words changed: " + str(upper_count) +
                "\nNumber of punctuations removed: " + str(punc_count) + "\nNumber of numbers removed: " + str(num_count) +
                "\nSpellchecking:#######" + "\nNumber of words: " + str(len(file_split)) + "\nNumber of correct words: " +
                str(true_word) + "\nNumber of incorrect words: " + str(false_word))







