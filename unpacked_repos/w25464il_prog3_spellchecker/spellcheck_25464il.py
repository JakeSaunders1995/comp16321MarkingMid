import argparse
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument("english",help="Path to EnglishWords.txt")
parser.add_argument("input_path",help="Path to input folder")
parser.add_argument("output_path",help="Path to output folder")
args = parser.parse_args()

valid = open(args.english,"r").read().rstrip().split("\n")

def main(input_file):
    data = open(args.input_path+"/"+input_file,"r").read()
    words = data.split(" ")

    upper = 0

    for x in words:
        if re.search("[A-Z]",x):
            upper += 1
    data = data.lower()

    punc = 0
    for x in range(len(data)):
        if re.search("[\",.!?#@'\[\]]",data[x]):
            punc += 1
    data = re.sub("[\",.!?#@'\[\]]","",data)

    num = 0
    for x in range(len(data)):
        if re.search("[0-9]",data[x]):
            num += 1
    data = re.sub("[0-9]","",data)
    data = re.sub(" +"," ",data)
    incorrect = 0

    words = data.split(" ")

    for x in words:
        if x not in valid:
            incorrect += 1

    string = """w25464il
Formatting ###################
Number of upper case words changed: %i
Number of punctuations removed: %i
Number of numbers removed: %i
Spellchecking ###################
Number of words: %i
Number of correct words: %i
Number of incorrect words: %i
""" % (upper,punc,num,len(words),len(words)-incorrect,incorrect)

    print(string)
    try:
        open(args.output_path+"/"+input_file[:-4]+"_w25464il.txt","x").write(string)
    except:
        open(args.output_path+"/"+input_file[:-4]+"_w25464il.txt","w").write(string)
        
for filename in os.listdir(args.input_path):
    main(filename)
