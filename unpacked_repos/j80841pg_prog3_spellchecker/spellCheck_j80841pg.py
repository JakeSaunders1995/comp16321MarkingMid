import os, glob, argparse, string
from pathlib import Path
punc = string.punctuation

parser = argparse.ArgumentParser()
parser.add_argument('wordfile', help="input file")
parser.add_argument('folderin', help="input folderpath")
parser.add_argument('folderout', help="output folderpath")
args = parser.parse_args()
words = args.wordfile
pathin = args.folderin
pathout = args.folderout
for filename in glob.glob(os.path.join(pathin, '*.txt')):
    with open(os.path.join(os.getcwd(), filename)) as f:
        namein = Path(filename).stem
        nameout = namein + "_j80841pg.txt"
        completeName = os.path.join(pathout, nameout)

        filein = open(filename)
        englishfile = open(words)
        fileout = open(completeName, "w")
        english = list(englishfile.read().split())
        text = filein.read()
        numupper = 0 #number of uppercase transformed
        numnum = 0 #number of numbers removed
        numpunc = 0 #number of punctuations removed
        numinc = [] #array for incorrect words
        numcor = [] #array for correct words
        check = False
        for i in text:
            if i.isupper():
                text = text.replace(i, i.lower())
                numupper += 1
            elif i.isdigit():
                text = text.replace(i, "")
                numnum += 1
            elif i in punc: #checking for punctuations
                text = text.replace(i, "")
                numpunc += 1
        text = " ".join(text.split()) #removing additional spaces between words
        text = text.split()
        for i in text:
            for j in english:
                if i == j:
                    check = True
            if check:
                numcor.append(i)
            else:
                numinc.append(i)
            check = False
        print(numinc)
        print(numcor)
        numwords = len(text)
        filein.close()
        englishfile.close()
        output = ["j80841pg\n", "Formatting ###################\n", "Number of upper case words transformed: ", str(numupper), "\n", "Number of punctuation’s removed:",
         str(numpunc), "\n", "Number of numbers removed: ", str(numnum), "\n", "Spellchecking ###################\n",
        "Number of words in file: ", str(numwords), "\n", "Number of correct words in file: ", str(len(numcor)), "\n",
        "Number of incorrect words in file: ", str(len(numinc)),  "\n"]
        fileout.writelines(output)
        fileout.close()

#Btw before finding out abour replace thing I wrote the whole code below ))
#for i in range(len(text)):
#for j in range(len(text[i])):
#if len(text[i]) == 0:
#        break
#if text[i][j].isupper():
#numupper += 1
#text[i]= text[i].lower()
#elif text[i][j].isdigit():
#current = list(text[i])
#while z < len(current):
#if len(current) == 0:
#            break
#elif current[z].isdigit():
#                print(current[j])
#                current.remove(current[z])
#                z -= 1
#            z += 1
#        current = "".join(current)
#        text[i] = current
