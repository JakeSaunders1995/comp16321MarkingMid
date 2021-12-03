import string
import sys
import os 

directory = sys.argv[2]
all_files = []
for filename in os.listdir(directory):
    input_file = os.path.join(directory, filename)
    if os.path.isfile(input_file):
        all_files.append(input_file)
for a in all_files:
    with open(a) as file:
        file  = file.read().replace('\n',' ')
    with open(sys.argv[1]) as f:
        f = f.readlines()

    word_dictionary = [x.strip('\n') for x in f]
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    numbers = string.digits
    punctuation = string.punctuation
    transform, num, pun = 0,0,0
    part1_check = str()

    for i in file:
        if i in lower_alphabet:
            part1_check += i
        elif i == ' ' and part1_check[-1] != ' ':
            part1_check += i
        elif i in upper_alphabet:
            part1_check += i.lower()
            transform += 1
        elif i in punctuation:
            pun += 1
        elif i in numbers:
            num += 1
            
    correct, incorrect = 0,0
    arr = part1_check.split(' ')
    for value in arr:
        if value in word_dictionary: correct +=1
        else: incorrect += 1
    
    filename = a[:-4]+'_z89079mb.txt'
    filename = filename.replace(sys.argv[2],sys.argv[3])
    with open(filename,'w') as fi:
        fi.write("z89079mb\n")
        fi.write("Formatting ###################\n")
        fi.write("Number of upper case words changed: "+str(transform)+"\n")
        fi.write("Number of punctuations removed: "+str(pun)+"\n")
        fi.write("Number of numbers removed: "+str(num)+"\n")
        fi.write("Formatting ###################\n")
        fi.write("Number of words: "+str(len(arr))+"\n")
        fi.write("Number of correct words: "+str(correct)+"\n")
        fi.write("Number of incorrect words: "+str(incorrect)+"\n")

