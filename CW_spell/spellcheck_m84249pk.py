import sys
import os
input_folder=sys.argv[2]
output_folder=sys.argv[3]
words=sys.argv[1]
count=0
for file in os.scandir(input_folder):
    file1=open(file,"r")
    count+=1
    pathname,filename=os.path.split(file)
    string=str(filename)
    string=string[0:len(string)-4]+"_m84249pk.txt"
    file2=open(output_folder+"/"+string,"w")
    sentence=str(file1.read())
    file3=open(words,"r")
    data=str(file3.read())
    Word_list=data.split("\n")
    def removeNumbers(sentence):
        string=""
        count=0
        for word in sentence:
            if not word.isdigit():
                string=string+word
            else:
                count+=1

        return count
    def removeNumbers2(sentence):
        string=""
        count=0
        for word in sentence:
            if not word.isdigit():
                string=string+word
            else:
                count+=1

        return string
    def removePunctuations(sentence):
        string=""
        count=0
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for word in sentence:
            if word in punc:
                count+=1
                sentence=sentence.replace(word,"")
        string=sentence


        return count
    def removePunctuations2(sentence):
        string=""
        count=0
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for word in sentence:
            if word in punc:
                count+=1
                sentence=sentence.replace(word,"")
                string=sentence
        return string
    def upperToLower(sentence):
        count=0
        string=""
        for word in sentence:
            if word.isupper():
                count+=1
                sentence=sentence.replace(word,word.lower())
                string=sentence

        return count
    def upperToLower2(sentence):
            count=0
            string=""
            for word in sentence:
                if word.isupper():
                    count+=1
                    sentence=sentence.replace(word,word.lower())
            string=sentence

            return string
    def isCorrect(sentence):
        count=0
        total=0
        spaces=0
        data1=sentence.split(" ")
        for word in data1:
            total+=1
            if word in Word_list:
                count+=1
            elif word in " " or word in "\n":
                spaces+=1
        file2.write("Number of words:"+" "+str(total-spaces)+"\n")
        return count
    def isIncorrect(sentence):
        count=0
        spaces=0
        total=0
        data1=sentence.split(" ")
        for word in data1:
            total+=1
            if word in Word_list:
                count+=1
            elif word in " " or word in "\n":
                spaces+=1
        return total-count-spaces
    def Display():
        file2.write("m84249pk"+"\n")
        file2.write("Formatting ###################"+"\n")
        file2.write("Number of upper case words changed:"+" "+str(upperToLower(sentence))+"\n")
        file2.write("Number of punctuations removed:"+" "+str(removePunctuations(sentence))+"\n")
        file2.write("Number of numbers removed:"+" "+str(removeNumbers(sentence))+"\n")
        #sent=removeNumbers(removePunctuations(upperToLower(sentence)))
        #file2.write(sent+"\n")
        file2.write("Spellchecking ###################"+"\n")
        file2.write("Number of correct words:"+" "+str(isCorrect(removeNumbers2(upperToLower2(removePunctuations2(sentence)))))+"\n")
        file2.write("Number of incorrect words:"+" "+str(isIncorrect(removeNumbers2(upperToLower2(removePunctuations2(sentence)))))+"\n")
        #isCorrect(sent)
    Display()
