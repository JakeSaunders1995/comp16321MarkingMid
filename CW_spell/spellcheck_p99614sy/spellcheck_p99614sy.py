import string
import sys
from os import listdir
from os.path import isfile, join
input_folder = sys.argv[2]
 
files = [file for file in listdir(input_folder) if isfile(join(input_folder, file)) and file[0] != '.']
eng_w = open(sys.argv[1]).read().splitlines()
 
 
 
 
list1 = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
list2 = ["1","2","3","4","5","6","7","8","9","0"]
 
def replace_ponc(lowText):
    punctuations = string.punctuation
    for i in punctuations:
        lowText = lowText.replace(i, '')
    for i in range(10):
        lowText = lowText.replace(str(i), '')
    return lowText
 
def uppernum(text):
    uppernum = 0
    for i in list1:
        for j in text:
            if i == j:
                uppernum += 1
    return uppernum
 
def punnum(text):
    punnum = 0
    for i in punctuations:
        for j in text:
            if i == j:
                punnum += 1
    return punnum
 
def numnum(text):
    numnum = 0
    for i in list2 :
        for j in text:
            if i == j:
                numnum += 1
    return numnum
 
 
def wrong(lowText, eng_w):
    nb = 0
    for i in lowText.split():
        if i not in eng_w:
            nb += 1
        else: pass
    return nb
 
for file in files:
    input_file = open(f"{input_folder}/{file}")
 
    text = input_file.readlines()
    lowText = text.lower()
    numnums = numnum(text)
    uppernums = uppernum(text)
    punnums = punnum(text)
 
    nb_words = len(replace_ponc(lowText).split())
    wordnumsin = wordnum(lowText, eng_w)
    wordnums = nb_words - wordnumsin
 
 
    answer = f"Formatting ###################\nNumber of upper case words transformed: {uppernums}\nNumber of punctuation’s removed: {punnums}\nNumber of numbers removed: {numnums}\nSpellchecking ###################\nNumber of words in file: {nb_words}\nNumber of correct words in file: {wordnums}\nNumber of incorrect words in file: {wordnumsin}"
 
    output_folder = sys.argv[3]
    output_file = open(f"{output_folder}/{file[:-4]}_n61655sb.txt", "w")
    output_file.write(answer)
 
    input_file.close()
    output_file.close()
