import os
import argparse

def format(name):
    f = open(name, "r")
    txt = f.read()
    f.close()
    upper = 0
    punc = 0
    num = 0
    result = ""
    for i in range(len(txt)):
        tmp = ord(txt[i])
        if (tmp >= 65 and tmp <= 90):
            upper += 1
            result += chr(tmp + 32)
        elif (tmp >= 48 and tmp <= 57):
            num += 1
        elif ((tmp >= 97 and tmp <= 122) or tmp == 32):
            result += chr(tmp)
        elif (tmp >= 33 and tmp != 127):
            punc += 1
    return (result, upper, punc, num)

def spellCheck(txt):
    sum = 0
    cor = 0
    inc = 0
    s = txt.split(" ")
    for i in s:
        if (i != ""):
            sum += 1
            if (i in engWords):
                cor += 1
            else:
                inc += 1
    return (sum, cor, inc)

def store(name, content):
    if (os.path.isfile(name)):
        f = open(name, "w")
        f.write("Formatting ###################\n")
        f.write("Number of upper case words transformed: " + str(content[0]) + "\n")
        f.write("Number of punctuation's removed: " + str(content[1]) + "\n")
        f.write("Number of numbers removed: " + str(content[2]) + "\n")
        f.write("Spellchecking ###################\n")
        f.write("Number of words: " + str(content[3]) + "\n")
        f.write("Number of correct words: " + str(content[4]) + "\n")
        f.write("Number of incorrect words: " + str(content[5]) + "\n")
        f.close()
    else:
        f = open(name, "x")
        f.write("Formatting ###################\n")
        f.write("Number of upper case words transformed: " + str(content[0]) + "\n")
        f.write("Number of punctuation's removed: " + str(content[1]) + "\n")
        f.write("Number of numbers removed: " + str(content[2]) + "\n")
        f.write("Spellchecking ###################\n")
        f.write("Number of words: " + str(content[3]) + "\n")
        f.write("Number of correct words: " + str(content[4]) + "\n")
        f.write("Number of incorrect words: " + str(content[5]) + "\n")
        f.close()

parser = argparse.ArgumentParser()
parser.add_argument("englishWords", help="increase English Words Text")
parser.add_argument("inputPath", help="increase input path")
parser.add_argument("outputPath", help="increase output path")
args = parser.parse_args()
currentPath = os.getcwd()
f = open(args.englishWords, "r")
engWords = []
for line in f:
    engWords.append(line.strip('\n'))
f.close()
os.chdir(args.inputPath)
pathList = os.listdir()
pathList.sort()
list1 = []
list2 = []
for text in pathList:
    list1.append(text)
    (pre, u, p, n) = format(text)
    (w, c, ic) = spellCheck(pre)
    list2.append([u, p, n, w, c, ic])
os.chdir(currentPath)
os.chdir(args.outputPath)
for i in range(len(list1)):
    if (list1[i][-4:] == ".txt"):
        tmp = list1[i][0:-4] + "_y70582kd.txt"
    else:
        tmp = list1[i] + "_y70582kd"
    store(tmp, list2[i])

