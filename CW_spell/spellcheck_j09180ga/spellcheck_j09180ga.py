import os
import string
import sys

punctuation = [".", "?", "!", ",", ":", ";", "—", "-", "(", ")", "[", "]", "{", "}", "'", '"', "…"]

englishwords = sys.argv[1]
inputfolder = sys.argv[2] + '/'
outputfolder = sys.argv[3] + '/'

for file in os.listdir(inputfolder):
    filepath = inputfolder + file
    with open(filepath) as f:
        counter = {}
        mydata = f.read()
        data = ""

        while mydata.find('...') != -1 or mydata.find('. . .') != -1:
            if mydata.find('...') != -1:
                mydata = mydata.replace('...', '')
                counter['punctuation'] = counter.get('punctuation', 0) + 1
            elif mydata.find('. . .') != -1:
                mydata = mydata.replace('. . .', '')
                counter['punctuation'] = counter.get('punctuation', 0) + 1

        for char in mydata:
            if char in punctuation:
                counter['punctuation'] = counter.get('punctuation', 0) + 1
            elif char in string.digits:
                counter['digit'] = counter.get('digit', 0) + 1
            elif char.isupper():
                counter['upper'] = counter.get('upper', 0) + 1
                data += char.lower()
            else:
                data += char

        with open(englishwords) as ff:
            dictionary = ff.read()
            dictionarywords = dictionary.split()
            for word in data.split():
                if word in dictionarywords:
                    counter['correct'] = counter.get('correct', 0) + 1
                else:
                    counter['incorrect'] = counter.get('incorrect', 0) + 1

    with open(outputfolder + file[0:-4] + "_j09180ga.txt", 'w') as f:
        f.write('j09180ga\n')
        f.write('Formatting ###################\n')
        f.write('Number of upper case words changed: ' + str(counter.get('upper', 0)) + '\n')
        f.write('Number of punctuations removed: ' + str(counter.get('punctuation', 0)) + '\n')
        f.write('Number of numbers removed: ' + str(counter.get('digit', 0)) + '\n')
        f.write('Spellchecking ###################\n')
        f.write('Number of words: ' + str(counter.get('correct', 0) + counter.get('incorrect', 0)) + '\n')
        f.write('Number of correct words: ' + str(counter.get('correct', 0)) + '\n')
        f.write('Number of incorrect words: ' + str(counter.get('incorrect', 0)) + '\n')
