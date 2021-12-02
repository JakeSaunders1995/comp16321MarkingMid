import sys
import os


def remove_punctuation(spellcheck_words):
    punctuations = '''!()-[]{};:'"\,<>./?$%^&*_~'''
    global no_punch_list
    no_punch_list = []
    no_punctuation = ""
    global num_punctuation
    num_punctuation = 0
    for word in spellcheck_words:
        character_num=0
        proceed = True
        if word[character_num]==".":
            if(word[character_num] and word[character_num+1] and word[character_num+2])==".":
                num_punctuation +=1
                proceed = False
            else:
                pass
        if proceed is True:
            for char in word:
                if char not in punctuations:
                    no_punctuation += char
                elif char in punctuations:
                    num_punctuation +=1


        no_punch_list.append(no_punctuation)
        no_punctuation=""

    return no_punch_list

def remove_number(no_punch_list):
    numbers = '''0123456789'''
    global no_num_list
    no_num_list = []
    no_numbers = ""
    global num_numbers
    num_numbers = 0
    for word in no_punch_list:
        for char in word:
            if char not in numbers:
                no_numbers += char
            elif char in numbers:
                num_numbers +=1

        no_num_list.append(no_numbers)
        no_numbers=""

    return no_num_list

def change_smallcase(no_numbers):
    capital = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    global small_case_list
    small_case_list = []
    small_case = ""
    global num_smallcase
    num_smallcase = 0
    for word in no_numbers:
        for char in word:
            if char in capital:
                small_case += char.lower()
                num_smallcase +=1
            else:
                small_case += char

        small_case_list.append(small_case)
        small_case = ""
    while("" in small_case_list) :
        small_case_list.remove("")
    return small_case_list

def spellcheck(small_case):
    for i in small_case:
        if i=='' :
            small_case.remove(i)
    global correct_words
    correct_words = 0
    global wrong_words
    wrong_words = 0
    global total_words
    total_words = len(small_case)
    file3=open("EnglishWords.txt", "r")
    data=str(file3.read())
    word_list=data.split("\n")

    for line in small_case:

        if line in word_list:
            correct_words += 1
        elif line not in word_list:
            wrong_words += 1

english_words = sys.argv[1]
inp_file = sys.argv[2]
ba= os.listdir(inp_file)
#os.mkdir(sys.argv[3])
for k in ba:
    r= inp_file+"/"+k
    with open(r,'r') as f:
        data = f.readlines()
        words= []
        for line in data:
            word = line.split(" ")
            words.append(word)
        spellcheck_words = []
        x= len(words)
        for i in range(x):
            y= len(words[i])
            fe = words[i]
            for z in range(y):
                last_word = words[i][z]
                spellcheck_words.append(last_word)
        for j in range(len(spellcheck_words)):
            spellcheck_words[j]=spellcheck_words[j].rstrip()
        empty_word = ''

        for n in spellcheck_words:
            if n == '' :
                spellcheck_words.remove(n)
        for n in spellcheck_words:
            if n == '' :
                spellcheck_words.remove(n)
        for n in spellcheck_words:
            if n == '' :
                spellcheck_words.remove(n)
        for n in spellcheck_words:
            if n == '' :
                spellcheck_words.remove(n)
        remove_punctuation(spellcheck_words)
        remove_number(no_punch_list)
        change_smallcase(no_num_list)
        spellcheck(small_case_list)
        g= k.replace('.txt','')
        w= sys.argv[3]+"/"+g+"_g39786dp"+".txt"
        x = open(w,'w')
        x.write("g39786dp"+"\n")
        x.write("Formatting ###################"+"\n")
        x.write("Number of upper case letters changed: "+str(num_smallcase)+"\n")
        x.write("Number of punctuations removed: "+str(num_punctuation)+"\n")
        x.write("Number of numbers removed: "+str(num_numbers)+"\n")
        x.write("Spellchecking ###################"+"\n")
        x.write("Number of words : "+str(total_words)+"\n")
        x.write("Number of correct words: "+str(correct_words)+"\n")
        x.write("Number of incorrect words: "+str(wrong_words)+"\n")
