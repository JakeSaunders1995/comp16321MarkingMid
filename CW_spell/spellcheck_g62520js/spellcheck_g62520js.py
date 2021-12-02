import argparse
import os
import re

parser = argparse.ArgumentParser(description='Input and Output files')
parser.add_argument('words', type=str, help='words file')
parser.add_argument('input', type=str, help='Input file')
parser.add_argument('output', type=str, help='Output file')
args = parser.parse_args()

EngWords = args.words
infile = args.input
outfile = args.output


words = open(EngWords,"r").read()
words_split = words.split("\n")
user = "g62520js"

def write_file(dir,file,user,output,up,punc,num,spell,total,right):
    if outfile[-1] == "/":
        out_name = outfile + x.split(".txt")[0] + "_" + user + ".txt"
        output_file = out_name
        directory = os.path.dirname(outfile)
    else:
        out_name = outfile + "/" + x.split(".txt")[0] + "_g62520js.txt"
        output_file = out_name
        directory = os.path.dirname(output_file)
        #print(directory)



    if not os.path.exists(directory):
        os.makedirs(directory)
    output = user + "\n" + "Formatting ###################\n" + "Number of upper case letters changed: " + str(up) + "\n" + "Number of punctuations removed: " + str(punc) + "\n" + "Number of numbers removed: " + str(num) + "\n" + "Spellchecking ################### \n" + "Number of words: " + str(total) + "\n" + "Number of correct words: " + str(right) + "\n" + "Number of incorrect words: " + str(spell)

    final_scores = open(output_file, "w")
    final_scores.write(output)
    final_scores.close()


numbers = ["1","2","3","4","5","6","7","8","9","0"]
punctuation = ".?!,:;-—[]{}()'\"…"



for x in os.listdir(infile):

    num_count = 0
    punc_count = 0
    word_count = 0
    upper_count = 0

    f = os.path.join(infile, x)
    dir_path = os.path.dirname(f)
    read_scores = open(f, "r")
    word_file = read_scores.readline()


    final = ""
    #print("\n")
    for i in word_file:
        if not i in numbers and not i in punctuation:
            if i != i.lower():
                upper_count += 1
                final += i.lower()
            else:
                final += i
        else:
            if not i in numbers:

                punc_count += 1
            if not i in punctuation:
                num_count += 1
                continue

    #print(final)
    sep_words = final.split()
    sep_words = re.sub('[^\w\s]',' ',final).split()

    total_words = len(sep_words)
    #print(total_words)
    correct = 0

    #print(sep_words)

    end = ""
    #print(sep_words)
    for y in sep_words:
        #print(y)
        if y in words_split:
            correct += 1
            #continue
        else:
            word_count += 1
            #print("spelt wrong", y)
    #print(end,upper_count,punc_count,num_count,word_count,total_words,correct)
    write_file(outfile,x,user,end,upper_count,punc_count,num_count,word_count,total_words,correct)
        
