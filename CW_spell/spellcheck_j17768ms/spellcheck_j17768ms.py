import string
import re


import argparse
import os

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", help="Enter Text File name")
    parser.add_argument("input_file", help="Enter input folder name")
    parser.add_argument("output_file", help="Enter output folder name")
    
    args = parser.parse_args()
    folder = str(args.input_file)
    outfolder = str(args.output_file)
    txt = str(args.text_file)
    files = os.listdir(folder)

    print(files)
    
    for file in files:
        my_file = open(folder + "/" + file, "r")

        content = my_file.read()

        d1 = open(txt, "r")
        d2 = d1.read()
        d3 = d2.split()


        q0 =re.findall("[^\w\s]",
                string = content)
        aa0 = "Number of punctuations removed "+str(len(q0))+"\n"
       
        q1 =re.findall("[\d]",
                string = content)
        aa1 = "Number of numbers rmeoved: "+str(len(q1))+"\n"
        
        q2 =re.findall("[A-Z]",
                string = content)
        aa2 = "Number of upper case words changed: "+str(len(q2))+"\n"
        


        sent = str(content)
        sent1 = sent.translate(str.maketrans('', '', string.punctuation))
        sent2 = ''.join([word for word in sent1 if not word.isdigit()])
        count = 0
        for index in range(len(sent2)-1) :
                if sent2[index+1].isspace() and not sent2[index].isspace():
                        count += 1 
        count+=1
        recount = int(count)
        srecount ="Number of words: "+str(recount)+"\n"

        c1 = sent2.lower()
        ct = c1.split()
        wct1 = 0
        for wrds in ct:
                if wrds in d3:
                        wct1+=1
        corwords=int(wct1)
        scorwords= "Number of correct words: "+str(corwords)+"\n"

        incwords= int(recount-corwords)
        sincwords="Number of incrrect words: "+str(incwords)+"\n"

        temp = file.split(".")
        output_file_name = temp[0] + "_" + "j17768ms" + "." + temp[1]
        outputfile = open(outfolder + "/" + output_file_name, "w+")
        outputfile.write("j17768ms"+"\n")
        outputfile.write("Formatting ###################"+"\n")
        outputfile.write(aa2)
        outputfile.write(aa0)
        outputfile.write(aa1)
        outputfile.write("Spellchecking ###################"+"\n")
        outputfile.write(srecount)
        outputfile.write(scorwords)
        outputfile.write(sincwords)

        

