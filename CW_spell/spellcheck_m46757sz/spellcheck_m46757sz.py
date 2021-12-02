import sys
import re
import os

def mk_paths(inpath,outpath):
    global in_paths, out_paths
    in_paths = []
    out_paths = []
    for i in os.listdir(inpath):
        if i[-4:] == ".txt":
            in_paths.append(inpath + "/" +i)
            out_paths.append(outpath + "/" + i[:-4] + "_m46757sz" + i[-4:])
    return

def read_file(path):
    with open(path,'r') as f:
        text = f.read()
    return text

def removal(text):
    global num_of_upper,num_of_punc,num_of_num
    def low(matched):
        return matched.group().lower()
    tup = re.subn('\d',"",text)
    text = tup[0]
    num_of_num = tup[1]
    tup = re.subn('[A-Z]',low,text)
    text = tup[0]
    num_of_upper = tup[1]
    tup = re.subn('[.]{3}',"",text)
    text = tup[0]
    num_of_punc = tup[1]
    tup = re.subn('[^a-z\n #@&]',"",text)
    text = tup[0]
    num_of_punc += tup[1]
    return text

def check(text,eng_words):
    global num_of_words,num_of_correct,num_of_incorrect
    words = text.split()
    num_of_words = len(words)
    num_of_correct = 0
    eng_words = eng_words.split()
    for i in words:
        for z in eng_words:
            if i == z:
                num_of_correct += 1
    num_of_incorrect = num_of_words - num_of_correct


def output(path):
    with open(path,'w') as f:
        f.write("m46757sz\n")
        f.write("Formatting ###################\n")
        f.write("Number of upper case letters changed: %d\n"%(num_of_upper))
        f.write("Number of punctuations removed: %d\n"%(num_of_punc))
        f.write("Number of numbers removed: %d\n"%(num_of_num))
        f.write("Spellchecking ###################\n")
        f.write("Number of words: %d\n"%(num_of_words))
        f.write("Number of correct words: %d\n"%(num_of_correct))
        f.write("Number of incorrect words: %d\n"%(num_of_incorrect))


def main(paths):
    word_path = paths[1]
    eng_words = read_file(word_path)
    mk_paths(paths[2],paths[3])
    for p in range(len(in_paths)):
        text = read_file(in_paths[p])
        text = removal(text)
        check(text,eng_words)
        output(out_paths[p])
    

if __name__ == "__main__":
    main(sys.argv)
