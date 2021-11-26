import sys
import os

eng_words_file_path = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]

input_list = os.listdir(input_path)
input_list.sort()
output_list = os.listdir(output_path)

string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string2 = ".?,!@\"\'\[\]#"
string3 = "1234567890"

with open(eng_words_file_path, "r") as er:
    eng_dic = er.readlines()

for i in range(len(eng_dic)):
    eng_dic[i] = eng_dic[i][0:-1] 

for file in input_list:
    with open(input_path + file, "r") as fr:
        data = fr.read()
    upper = 0
    punc = 0
    numbers = 0
    del_ch = set()
    for i in range(len(data)):
        if data[i] == " ":
            continue
        elif data[i] in string1:
            upper += 1
        elif data[i] in string2:
            del_ch.add(data[i])
            punc += 1
        elif data[i] in string3:
            del_ch.add(data[i])
            numbers += 1
    
    for ch in del_ch:
        data = data.replace(ch, '')
    
    data = data.lower()
        
    words_list = data.split(" ")
    for w in words_list:
        if w == '':
            words_list.remove(w)
    num_words = len(words_list)
    num_c_words = 0
    num_i_words = 0
    for i in range(num_words):
        if words_list[i] in eng_dic:
            num_c_words += 1
        else:
            num_i_words += 1
            
    output_file = file[0:10] + '_[j29115zl]' + file[10:]
    with open(output_path + output_file, "w+") as fw:
        fw.write("[user_name]\n")
        fw.write("Formatting ###################\n")
        fw.write("Number of upper case words transformed:  " + str(upper) + "\n")
        fw.write("Number of punctuation’s removed:  " + str(punc) + "\n")
        fw.write("Number of numbers removed:  " + str(numbers) + "\n")
        fw.write("Spellchecking ###################" + "\n")
        fw.write("Number of words in file:  " + str(num_words) + "\n")
        fw.write("Number of correct words in file:  " + str(num_c_words) + "\n")
        fw.write("Number of incorrect words in file:  " + str(num_i_words) + "\n")
        
