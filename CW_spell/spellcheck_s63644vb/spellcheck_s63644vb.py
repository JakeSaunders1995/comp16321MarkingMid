import sys
import os

def formattext(input_file):
    punc=[".","?","!",",",":",";","-","--","'","''","[","]","{","}","(",")",'"',"...","[]","{}","()",'""']
    upperc=0
    punctuations=0
    numbers=0
    f_in=open(input_file,"r")
    newdata=[]
    for line in f_in:
        linedata=""
        for word in line:
            newword=""
            if word in punc:
                punctuations+=1
            else:
                if word.isnumeric():
                    numbers+=1
                elif word.isupper() and word.isalpha():
                    upperc+=1
                    newword+=word.lower()
                else:
                    newword+=word
            linedata+=newword
        newdata.append(linedata)

    f_out=open(input_file,"w")
    for i in newdata:
        f_out.write(i)
    f_out.close()
    fin_data=[upperc,punctuations,numbers]
    return fin_data

def scheckfile(words,input_file,output_folder,file_data,txtfile):
    dict_file=open(words,'r')
    spellcwords=list(dict_file.read().split())
    f_in=open(input_file,"r")
    wordsinfile=[]
    correctw=0
    incorrectw=0
    for i in f_in:
        for j in i.split(sep=" "):
            if not j.isalpha or j=="" or j==" " or j=="\n":
                pass
            else:
                wordsinfile.append(j)

    totalwords=len(wordsinfile)
    for x in wordsinfile:
        if x in spellcwords:
            correctw+=1
        else:
            incorrectw+=1
    numbers=file_data[2]
    punctuations=file_data[1]
    upperc=file_data[0]
    f_in.close()
    output_file=output_folder+"/"+txtfile[:-4]+"_s63644vb.txt"
    f_out=open(output_file,"w")
    f_out.write("s63644vb\n")
    f_out.write("Formatting ###################\n")
    f_out.write("Number of upper case letters changed: "+str(upperc)+'\n')
    f_out.write("Number of punctuations removed: "+str(punctuations)+'\n')
    f_out.write("Number of numbers removed: "+str(numbers)+'\n')
    f_out.write("Spellchecking ###################\n")
    f_out.write("Number of words: "+str(totalwords)+'\n')
    f_out.write("Number of correct words: "+str(correctw)+"\n")
    f_out.write("Number of incorrect words: "+str(incorrectw))
    f_out.close()


arg_list=(sys.argv)
parent_path=os.getcwd()
words=arg_list[1]
input_folder=arg_list[2]
output_folder=arg_list[3]

os.chdir(input_folder)
for txtfile in os.listdir():
    if txtfile.endswith(".txt"):
        os.chdir(parent_path)
        input_file=f"{input_folder}/{txtfile}"
        file_data=formattext(input_file)
        scheckfile(words,input_file,output_folder,file_data,txtfile)