import argparse
import os
#pathsetting
parser = argparse.ArgumentParser()
parser.add_argument('filepath1')
parser.add_argument('filepath2')
parser.add_argument('filepath3')
args = parser.parse_args()
dictpath = args.filepath1
inputpath = args.filepath2
outputpath = args.filepath3
inputfiles = os.listdir(inputpath)

#number(48-57), punctuation(32-47, 58-64, 91-96, 123-126 )
def removeNum(string):
    result = ""
    count = 0
    for x in string:
        if (ord(x) > 47) and (ord(x) < 58) :
            if ord(x) != 35 and ord(x) != 64:
                count = count + 1
        else:
            result = result + x
    return result, count

def removePunc(string):
    result = ""
    count = 0
    count_dot = 0
    for x in string:
        if x == ".":
            count_dot = count_dot + 1
        else:
            count_dot = 0
        if count_dot == 3:
            count = count - 2
        if ((ord(x) > 32) and (ord(x) < 48)) or ((ord(x) > 57) and (ord(x) < 65)) or ((ord(x) > 90) and (ord(x) < 97)) or ((ord(x) > 122) and (ord(x) < 124)):
            count = count + 1
        else:
            result = result + x
    return result, count

def toLower(string):
    result = ""
    count = 0
    for x in string:
        current = x.lower()
        if x == current:
            result = result + x
        else:
            count = count + 1
            result = result + current
    return result, count

def splitString(string):
    thislist=[]
    current = ""
    for x in string:        
        if (ord(x) > 96 and ord(x) < 123) or ord(x) == 35 or ord(x) == 64:
            current = current + x
        elif x == " ":
            if current != "":
                thislist.append(current)
                current = ""
        elif ord(x) == 10:
            if current != "":
                thislist.append(current)
                current = ""
    if current!="":
        thislist.append(current)
    return thislist    

def checkSpell(checklist, checkdict):
    count = 0
    for x in checklist:
        for word in checkdict:
            if x == word:
                count = count + 1
                break            
    return count

#create dictionary list
myEngDict= []
with open(dictpath) as file:
    for line in file:
        myEngDict.append(line.rstrip())
file.close()

#input data
os.chdir(inputpath)
for files in inputfiles: 
    with open(files) as file:
    	line = file.read()
    file.close()

    mystring, count_num = removeNum(line)
    mystring, count_punc = removePunc(mystring)
    mystring, count_lower = toLower(mystring)
    mylist = splitString(mystring)
    numWord = len(mylist)
    count_correct = checkSpell(mylist, myEngDict)
    count_incorrect = numWord - count_correct

#final output data
    filesname = str(files)
    name = filesname[0:-4] + "_m73289ls.txt"
    os.chdir(outputpath)
    with open(name, 'w') as file:
        file.write("m73289ls\n")
        file.write("Formatting ###################\n")  
        file.write("Number of upper case words changed: " + str(count_lower) + "\n")
        file.write("Number of punctuation’s removed: " + str(count_punc) + "\n")       
        file.write("Number of numbers removed: " + str(count_num) + "\n")
        file.write("Spellchecking ###################\n")
        file.write("Number of words in file: " + str(numWord) + "\n")
        file.write("Number of correct words in file: " + str(count_correct) + "\n")
        file.write("Number of incorrect words in file: " + str(count_incorrect) + "\n")
    file.close()
    os.chdir(inputpath)
