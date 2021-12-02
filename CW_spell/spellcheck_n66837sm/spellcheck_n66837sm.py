import os
import os.path
import shutil
import re 
import string
def find_and_open(filename):
    for rf, folders, files in os.walk('.'):
        if filename in files:
            with open(rf + '/' + filename) as f:
            	f.read()
def create_and_write(filename):
    for rf, folders, files in os.walk('.'):
        if filename in files:
            with open(rf + '/' + filename) as w:
            	w.write()
def compare(content):
            correct =0
            for word in content:
                #print(word)
                i=0
                while i<len(newlist):
                    if word==newlist[i]:
                        correct+=1
                        i+=1
                    else:
                        i+=1
            #print(correct)
            return correct

files_and_directories = os.listdir("input_folder")
sortedfiles = sorted(files_and_directories)


numbers = str("1234567890")
punctuation = ['...','"',"'",'(',')','{','}','[',']','-','_','.',',','!','?',';',':','/']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
with open("EnglishWords.txt") as engwords:
	lines = engwords.readlines()
#print(type(lines))
for naming in sortedfiles:
    os.path.splitext(naming[0])
    naming = os.path.splitext(naming)[0]

for filename in sortedfiles:
    with open(os.path.join("input_folder", filename),'r') as f:
        with open(filename, "a") as newline:
	        newline.write("\n")
	        rd = f.read()
#count uppercase
        countupper = sum(1 for elem in rd if elem.isupper())
        #print("upper" + str(countupper))
#count punctuation
        count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
        countpunc = count(rd, string.punctuation)
        #print("punctuation" +str(countpunc))
        countdigit =0
        for char in rd:
        	if char.isdigit():
        		countdigit+=1 
        	else:
        		pass
        #print("digit" +str(countdigit))
        
        updated=""
        for char in rd:
        	if char not in punctuation:
        		updated = updated + char
        #print(updated)
        uptolower = ""
        for i in range (len(rd)):
        	if rd[i].isupper():
        		uptolower+=rd[i].lower()
        	else: 
        		uptolower+=rd[i]
        	updated = uptolower
        #print(updated)
        updated = ''.join([i for i in updated if not i.isdigit()])
        #print(updated)
        updated = ''.join([i for i in updated if i not in punctuation])
        updated = re.sub(r'\s+', ' ', updated)
        #print(updated)
        wordlist= updated.split()
        countwords= len(wordlist)
        #print("word" + str(countwords))
        with open("EnglishWords.txt") as f:
            file = f.readlines()
            newlist = []
            for element in file:
                newlist.append(element.strip())
        comparing = str(updated)
        correct = re.split("\s", comparing) 
        compare(correct)
        correctwd = int(compare(correct))
        incorrect = countwords -correctwd
        print(correctwd)
        c5=correctwd
        def output(c1, c2, c3,c4,c5,c6):
            files_and_directories = os.listdir("input_folder")
            sortedfiles = sorted(files_and_directories)
            with open(filename+"_n66837sm.txt", "w") as p:
                #p.write("%s%s%s%s%s%s"%(c1, c2, c3,c4,c5,c6))
                p.write("n66837sm\nFormatting ###################\nNumber of upper case letters changed: %s\nNumber of punctuations removed: %s\nNumber of numbers removed: %s\nSpellchecking ###################\nNumber of words: %s\nNumber of correct words: %s\nNumber of incorrect words: %s\n"%(countupper, countpunc, countdigit,countwords,correctwd,incorrect))
                naming = filename+"_n66837sm.txt"
                change = shutil.move(naming, 'output_folder')
            return output
        output(countupper, countpunc, countdigit,countwords,c5,incorrect)
