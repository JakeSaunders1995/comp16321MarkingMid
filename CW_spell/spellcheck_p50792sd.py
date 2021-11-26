#do the commandline bit input and output and research how to add the english.txt file too
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("english",type=str)
parser.add_argument("input",type=str)
parser.add_argument("output",type=str)

args = parser.parse_args()

import os

#counts the number of files in input
directory = args.input
totalFiles = 0

inputcount = 0
dir = args.input
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir,path)):
        inputcount+=1
#print(inputcount)

#counts the number of files in output

totalFiles = 0

outputcount = 0
dir = args.output
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir,path)):
        outputcount+=1
#print(outputcount)



#interate through input files in input folder
for filename in os.scandir(directory):
    #print(filename)

    #if the file exists then run the programm to get it formatted
    if filename.is_file():


        file = open(filename, "r")
        # file = open(args.input,"r")
        dictionary = open(args.english, "r")
        text = ""
        for line in file:
            # line=line.rstrip()
            text = line

        englishwords = []
        dictionary = open("EnglishWords.txt", "r")
        for line in dictionary:
            line = line.rstrip()
            englishwords.append(line)


        # this gets rid of caps
        uppertransformed = 0
        lower_text = text.lower()
        for i in range(len(text)):
            if text[i] != text[i].lower():
                uppertransformed = uppertransformed + 1
            elif text[i] == text[i].lower():
                continue

        # print(uppertransformed)

        # print(lower_text)

        # check the re documentation

        # this gets rid of numbers
        pattern = r'[0-9]'
        nonum_string = re.sub(pattern, '', lower_text)
        # print(nonum_string)
        # print(new_string)
        # pattern = re.compile(new_string)
        numbers = "1234567890"
        numbertransformed = 0
        for i in range(len(lower_text)):
            if lower_text[i] in numbers:
                #print(lower_text[i])
                numbertransformed = numbertransformed + 1
            elif lower_text[i] not in numbers:
                continue
        # print(numbertransformed)

        # this gets rid of punctuation
        punctuation = '''!()-[]{}+_=;:'"\,.<>?/@£$%^&*€#!'''
        puntransform = 0
        nopunt_string = ""
        for i in nonum_string:
            if i not in punctuation:
                nopunt_string = nopunt_string + i
            elif i in punctuation:
                puntransform = puntransform + 1
        # print(nopunt_string)
        # print(puntransform)
        # print(nopunt_string.split())
        list = nopunt_string.split()
        # print(list[0])
        words = 0
        correct_words = 0
        incorrect_words = 0
        for i in range(len(list)):
            if list[i] in englishwords:

                words = words + 1
                correct_words = correct_words + 1
            elif list[i] not in englishwords:
                #print(list[i])
                words = words + 1
                incorrect_words = incorrect_words + 1

        # print(words)
        # print(correct_words)
        # print(incorrect_words)

        # outputFile = open(args.output, "w")
        # print(
        #     "p50792sd", "\n"
        #     "Formatting ###################", "\n"
        #     "Number of upper case words changed: ", uppertransformed, "\n"
        #     "Number of punctuations removed: ",puntransform, "\n"
        #     "Number of numbers removed: ", numbertransformed, "\n"
        #     "Spellchecking ###################", "\n"
        #     "Number of words: ",words, "\n"
        #     "Number of correct words: ", correct_words, "\n"
        #     "Number of incorrect words: ", incorrect_words, "\n",
        #     file=outputFile
        # )
        # outputFile.close()
        #

        dict = args.output
        obj = os.scandir(dict)
        f = filename.name.split(".")

        #print(os.listdir(dict)[0])
        if outputcount<inputcount:
            #print("b")
            for u in range(inputcount):
                username = '_p50792sd'
                outputfilename = ""
                f = filename.name.split(".")
                outputfilename = outputfilename + f[0]
                outputfilename = outputfilename + username
                arguments = outputfilename + ".txt"
                arguments = args.output + '/' + arguments
                #print(arguments)
                file = open(arguments, "x")
                break
        obj = os.scandir(dict)
        for entry in obj:
            e = entry.name.split("_")
            file_output = e[0] + "_" + e[1]
            # print(entry)
            # if entry.name[0:9]=="test_file":
            #     print("a")
            #     #continue
            # elif entry.name == ".DS_Store":
            #     pass
            #
            # else:
            #     print("b")
            #     for u in range(inputcount):
            #         username = '_p50792sd'
            #         outputfilename = ""
            #         outputfilename=outputfilename +(filename.name[0:10])
            #         outputfilename = outputfilename + username
            #         arguments = outputfilename+".txt"
            #         arguments = args.output+'/'+arguments
            #         print(arguments)
            #         file = open(arguments, "x")
            #         break
            #obj = os.scandir(dict)
            #print(entry)
            #print(entry.name)

            if f[0] == file_output:
            #if filename.name[0:10] == entry.name[0:10]:
                #print(filename.name[0:10])
                #print(entry.name[0:10])
                #print("88888888888")

                outputFile = (open(entry, "w+"))

                print(
                    "p50792sd", "\n"
                    "Formatting ###################", "\n"
                    "Number of upper case letters changed:",uppertransformed, "\n"
                    "Number of punctuations removed:", puntransform, "\n"
                    "Number of numbers removed:",numbertransformed, "\n"
                    "Spellchecking ###################", "\n"
                    "Number of words:", words, "\n"
                    "Number of correct words:",correct_words, "\n"
                    "Number of incorrect words:", incorrect_words, "\n",
                    file=outputFile
                )
            else:
                continue


           # print(entry)
            #if entrys name as a string from index test_file

            #print(entry[1])
        #     if  entry.is_file():
        #         print(entry.name)
        # # filename2 = entry.name
        # # if filename2.is_dir()or filename2.is_file():
        # # #if filename2.is_file():
        #
        #         outputFile = open(entry, "w+")
        #
        #         print(
        #         "p50792sd", "\n"
        #         "Formatting ###################","\n"
        #         "Number of upper case words changed:",uppertransformed,"\n"
        #         "Number of punctuations removed:", puntransform,"\n"
        #         "Number of numbers removed:",numbertransformed,"\n"
        #         "Spellchecking ###################","\n"
        #         "Number of words:",words,"\n"
        #         "Number of correct words:",correct_words,"\n"
        #         "Number of incorrect words:", incorrect_words,"\n",
        #         file=outputFile
        #         )
        #         #outputFile.close()
                #print("d")
                #print(os.listdir(dict)[1])
                #if os.listdir(dict)[0] == i:
            #
                #break
            break
        #break
    #continue