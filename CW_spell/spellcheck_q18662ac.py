import argparse
import os

parse = argparse.ArgumentParser()
parse.add_argument("input_folder",help = "The folder which contains the inputs")
parse.add_argument("output_folder",help = "The folder which will contains the Output")
args  = parse.parse_args()

def format(f):
    data = f.read()
    counter1 = 0 #No. of Nos. removed
    counter2 = 0 #No. of symbols removed
    string = ""
    list1 = ["0","1","2","3","4","5","6","7","8","9"]
    list2 = [".",",","/","<",">","?","(",")","!","@","#","$","%","^","&","*","`","~","{","}","[","]","|",":",";","_","-","+","=",'"',"'"]
    counter3 = 0 #No.of upper case letters
    for i in range (len(data)):
        if data[i] in list1:
            counter1 +=1
        elif data[i] in list2:
            if data[i] == ".":
                if (i+2) < len(data): 
                    if data[i+1] == "." and data[i+2] == ".":
                        counter2 += -2
            counter2 += 1
        elif data[i].isupper():
            counter3 += 1

    for i in range (len(data)):
        if data[i].isalpha() or data[i] == " ":
            string += data[i]
    string = string.lower()
    
    f2 = open("EnglishWords.txt","r")
    list = f2.read()
    words = string.split()
    list = list.split() #Won't consider substrings
    counter5 = len(words) #No. of words
    counter4 = 0 #No. of incorrect words
    for i in words:
        if i not in list:
            counter4 += 1
    counter6 = counter5 - counter4 #No. of incorrect words
    f2.close()

    newstr1 = "Number of upper case letters changed: " + str(counter3)
    newstr2 = "Number of punctuations removed: "+ str(counter2)
    newstr3 = "Number of numbers removed: "+ str(counter1)
    newstr4 = "Number of words: " + str(counter5)
    newstr5 = "Number of correct words: " +str(counter6)
    newstr6 = "Number of incorrect words: " + str(counter4)
    newstr = "Q18662ac\nFormatting ###################\n" + newstr1+"\n" + newstr2+ "\n" + newstr3+"\n" + "Spellchecking ###################\n" + newstr4+"\n" + newstr5+"\n" + newstr6
    return newstr


for file in os.scandir(args.input_folder):
    file1=open(file,"r")
    pathname,filename=os.path.split(file)
    string=str(filename)
    string=string[0:len(string)-4]+"_q18662ac.txt"
    file2=open(args.output_folder+"/"+string,"w")
    file2.write(format(file1))
    file1.close()
    file2.close()