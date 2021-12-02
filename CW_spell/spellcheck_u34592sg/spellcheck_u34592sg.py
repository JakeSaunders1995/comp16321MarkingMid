## Spellchecker_u34592sg ##
import sys
import os
eng = sys.argv[1]
infile = sys.argv[2]
oufile = sys.argv[3]
puntuation = " !@#$%^&*()_+-=[]\{}|;':,./<>?~`"
l = os.listdir(infile)
list1 = l
with os.scandir(infile) as entries:
    for i in entries:
        print(i)
        over_all_count = 0
        pun_count = 0
        num_count = 0
        cap_count = 0
        f = open(i , "r")
        st = os.path.basename(i)[:-4]
        fw = open(oufile + "/" + st + "_u34592sg.txt" , "w")
        f1 = open("EnglishWords.txt", "r")
        dummy_list = f1.readlines()
        word_list = list(map(str.strip,dummy_list))
        o = f.readline().split(" ")  
        v = []
        for j in o:
            for i in j:
                if i in puntuation:
                    j = j.replace(i , "")
                    pun_count += 1
                elif i.isdigit() == True:
                    j = j.replace(i , "")
                    num_count += 1
                elif i.isupper() == True:
                    cap_count += 1
                    j = j.replace(i,i.lower())
            v.append(j)

        while "" in v:
            v.remove("")
        lenth = len(v)


        for k in v:
            if k not in word_list:
                over_all_count += 1
            else:
                continue

       
        fw.write("Formatting#########################\n")
        fw.write("The number of Puntuation removed: " + str(pun_count)+ "\n")
        fw.write("The number of numbers removed: " + str(num_count)+ "\n")
        fw.write("The number of upper case word transformed: " + str(cap_count)+ "\n")
        fw.write("Spellchecking####################### \n")
        fw.write("Total number of words in file: " + str(lenth)+ "\n")
        fw.write("Total number of correct words in file: " + str(lenth - over_all_count ) +"\n")
        fw.write("Total number of incorrect words in file: " +  str(over_all_count) +"\n")
        f.close()
        fw.close()


