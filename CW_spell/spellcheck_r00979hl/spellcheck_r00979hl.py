# a python program written by Hanmin Liu
# spellCheck
import os
import argparse
#initialize arguments
parser = argparse.ArgumentParser()
parser.add_argument("din", help="state where the EnglishWords.txt here")
parser.add_argument("fin", help="state where the input file here")
parser.add_argument("fout", help="state where the output file here")
args = parser.parse_args()

input_folder = os.scandir(args.fin)
#dict = os.scandir(args.din)

d = open(args.din)

"""
for names in dict_folder:
    if("EnglishWords" in names.name):
        d = open(names.name)
        break
"""
dict = d.read().split("\n")
for input_name in input_folder:
    #if("test" in input_name.name):
    if(True):
        f = open(input_name)
        output_name = input_name.name.replace(".txt","_r00979hl.txt")
        g = open(str(args.fout)+"/"+output_name, "w")
        strIn = f.read()

        # main body begin
        # formatting
        g.write("r00979hl\n")
        g.write("Formatting ###################")
        # counting
        counter_num = 0
        counter_pun = 0
        counter_upper = 0
        # print(strIn)

        i = 0
        while(i < len(strIn)):
            #print(i,end=' ')
            #print(len(strIn),end=' ')
            #print(strIn[i])
            if(strIn[i] == '\n'):
                i += 1
                continue
            x = ord(strIn[i])
            #count the upper case
            if(x >= 65 and x <= 90):
                counter_upper += 1
                strIn = strIn[:i] + chr(x+32) + strIn[i+1:]
                #print(strIn)
            elif(x >= 48 and x <= 57):
                counter_num += 1
                strIn = strIn[:i]+strIn[i+1:]
                i -= 1
                #print(strIn)
            elif(x == 32 or (x >= 97 and x <= 122)):
                i += 1
                continue
            else:
                strIn = strIn[:i]+strIn[i+1:]
                i -= 1
                counter_pun += 1
                #print(strIn)
                #print(counter_pun)
            i += 1
        #Formatting
        g.write("\nNumber of upper case letters changed: ")
        g.write(str(counter_upper))
        g.write("\nNumber of punctuations removed: ")
        g.write(str(counter_pun))
        g.write("\nNumber of numbers removed: ")
        g.write(str(counter_num))
        g.write("\nSpellchecking ###################")
        # counting
        correct = 0
        incorrect = 0
        str_list = strIn.split(" ")
        #print(strIn)
        for word in str_list:
            if word == '' or word == '\n':
                continue
            if word in dict:
                    correct += 1
                    #print(word)
            else:
                incorrect += 1
                #print(word)
        #formatting
        g.write("\nNumber of words: ")
        g.write(str(correct + incorrect))
        g.write("\nNumber of correct words: ")
        g.write(str(correct))
        g.write("\nNumber of incorrect words: ")
        g.write(str(incorrect))
        # main body end

        # file closing
        f.close()
        g.close()
d.close()
