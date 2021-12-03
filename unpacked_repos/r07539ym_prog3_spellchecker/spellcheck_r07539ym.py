import string
import sys, os

with open(sys.argv[1],"r") as english_words:
    english_words = english_words.read().split("\n")
input_path = sys.argv[2]
output_path = sys.argv[3]
list_punc = list(string.punctuation)
list_punc.remove("@")
list_punc.remove("#")


for file in os.listdir(input_path):
    num_nums = 0
    num_punc = 0
    num_words = 0
    num_upper = 0
    num_incorrect = 0
    num_correct = 0
    parsed_contents = ""
    with open(os.path.join(input_path, file), "r") as text_file:
        contents = text_file.read()

    for i in range(len(contents)):
        if contents[i] in list(string.ascii_lowercase) or contents[i] == " ":
            parsed_contents+=contents[i]
        elif contents[i] in list(string.ascii_uppercase):
            parsed_contents+=contents[i].lower()
            num_upper += 1
        elif contents[i] in list(string.digits):
            num_nums +=1
        elif contents[i] in list_punc:
            try:
                if contents[i]==contents[i+1]==contents[i+2] == ".":
                    num_punc-=2
                    if contents[i-1]!=" ":
                        parsed_contents+=" "
                elif contents[i]==contents[i+2]==contents[i+4]=="." and contents[i+1] == contents[i+3] == " ":
                    num_punc-=2
            except:
                pass
            num_punc+=1
    contents_list = parsed_contents.split()
    print(contents_list)
    for word in contents_list:
        if word in english_words:
            num_correct+=1
        else:
            num_incorrect +=1

    num_words = len(contents_list)
    num_correct = num_words-num_incorrect

    file_output = """
r07539ym
Formatting ###################
Number of upper case letters changed: {}
Number of punctuations removed: {}
Number of numbers removed: {}
Spellchecking ###################
Number of words: {}
Number of correct words: {}
Number of incorrect words: {}
                """.format(num_upper,num_punc,num_nums,num_words,num_correct,num_incorrect).lstrip()
    file_name = output_path+"\{}".format(file.split(".")[0]+"_r07539ym.txt")
    with open(file_name,"w+") as output_file:
        output_file.write(file_output)
        os.rename(file_name,"{}".format(file.split(".")[0]+"_r07539ym.txt"))
