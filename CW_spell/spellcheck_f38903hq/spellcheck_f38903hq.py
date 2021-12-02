import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('Englishwords')
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()
Englishwords = args.Englishwords
inputFolder = args.input_folder
outputFolder = args.output_folder
z = os.listdir(inputFolder)
list1 = []
Words = open(Englishwords, "r")
for k in Words:
    k = k.rstrip()
    list1.append(k)
for j in z:
    os.chdir(inputFolder)
    with open(j) as files:
        lines = files.read()
        str = lines
        n1 = 0
        upper_case_words = """A、B、C、D、E、F、G、H、I、J、K、L、M、N、O、P、Q、R、S、T、U、V、W、X、Y、Z"""
        for word in str:
            if word in upper_case_words:
                n1 = n1 + 1

        punctuations = '''!()-[]{};:'"\,<>./?_~#'''
        n = 0
#        str = input('message')
        for char in str:
            if char in punctuations:
                n = n + 1

        n2 = 0
        number = """1234567890"""
        for num in str:
            if num in number:
                n2 = n2 + 1

        punctuations = '[,./;\]1234567890[)(#:"]'
        str2 = re.sub(punctuations, '', str).lower()
        str3 = str2.split()

        n3 = 0
        n4 = 0

        str3 = str2.strip().split()

        for z in str3:
            if z in list1:
                n3 += 1
            else:
                n4 += 1

    os.chdir(outputFolder)
    b = os.listdir(outputFolder)
    filename = j
    outputName = filename[:-4] + "f38903hq.txt"
    with open(outputName, 'w') as t:
        t.write("️f38903hq\nFormatting ###################\n")
        t.write("Number of upper case words transformed: %d\n" %n1)
        t.write("Number of punctuation’s removed: %d\n" %n)
        t.write("Number of number's removed: %d\n" %n2)

        t.write("Spellchecking ###################\n")
        t.write("Number of words in file: %d\n" % len(str3))

        t.write("Number of correct words in file: %d\n"%n3)
        t.write("Number of incorrect words in file: %d"%n4)
