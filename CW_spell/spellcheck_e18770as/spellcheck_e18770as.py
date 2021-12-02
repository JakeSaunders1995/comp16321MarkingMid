import sys
import os
list_input=sys.argv
input_directory= sys.argv[2]
output_directory= sys.argv[3]
englishword=str(sys.argv[1])
filenames=[]
outputpaths=[]
paths=[]
for entry in os.listdir(input_directory):
    if (entry.endswith(".txt")):
        path1=(os.path.join(input_directory,entry))
        paths.append(path1)
        filename= entry.split(".")[0]
        outputfilename=filename+"_e18770as.txt"
        outputpath=(os.path.join(output_directory,outputfilename))
        outputpaths.append(outputpath)
        filenames.append(filename)

length=len(filenames)

for i in range(length):
    input_file=paths[i]
    output_file=outputpaths[i]
    fin= open(input_file, "r")
    fout=open(output_file,"w")
    fin1=open(englishword,"r")
    englishwords=fin1.read().split()
    contents=fin.read()
    punctuations=(".","...","?","!",",",":",";","-","—","_","(",")","{","}","[","]","'",'"')
    count_words=0
    count_numbers=0
    count_punctuations=0
    count_uppercase=0
    count_correct=0
    count_incorrect=0
    new_contents=""
    final_contents=""
    length=len(contents)
    while i< length:
        """for i in contents:"""
        if ord(contents[i]) >=65 and ord(contents[i])<=90:
            new_contents=new_contents+contents[i]
            i+=1
        elif ord(contents[i]) >= 97 and ord(contents[i])<= 122:
            new_contents=new_contents+contents[i]
            i+=1
        elif ord(contents[i]) == 32 or contents[i]=="\n":
            new_contents=new_contents+contents[i]
            i+=1
        elif ord(contents[i])>=48 and ord(contents[i])<= 57:
            count_numbers+=1
            i+=1
        elif contents[i] in punctuations:
            if i+2 < length and contents[i]=="." and contents[i+1]=="." and contents[i+2]==".":
                    count_punctuations+=1
                    i+=3
            else:
                count_punctuations+=1
                i+=1
        else:
            i+=1

    for letter in new_contents:
        if letter.isupper():
            count_uppercase+=1
            lowercase=letter.lower()
            final_contents=final_contents + lowercase
        else:
            final_contents=final_contents + letter
            
    list1= final_contents.split()

    for i in list1:
        if i in englishwords:
            count_correct+=1

        else:
            count_incorrect+=1
    fout.write("e18770as" + "\n")
    fout.write("Formating ###################" + "\n")
    fout.write("Number of upper case words changed: "+str(count_uppercase) + "\n")
    fout.write("Number of punctuations removed: " +str(count_punctuations) + "\n")
    fout.write("Number of numbers removed: " +  str(count_numbers) + "\n")
    fout.write("Spellchecking ###################" + "\n")
    fout.write("Number of words: " + str(len(list1)) + "\n")
    fout.write("Number of correct words: " + str(count_correct) + "\n")
    fout.write("Number of incorrect words: " +str(count_incorrect) + "\n")
    fin.close()
    fin1.close()
    fout.close()
