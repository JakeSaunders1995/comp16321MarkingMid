import argparse , os

#Spelling Checker

parser = argparse.ArgumentParser(description='Takes file that contains sentences and spell checks with given english file')
parser.add_argument('engDic', type = argparse.FileType('r'), help="Takes english words file")
parser.add_argument('inpath', help="takes input folder path (contains sentences in files)")
parser.add_argument('outpath', help="takes output folder path (formatting files results generated here)")
args = parser.parse_args()

#Accessing Input Files
cwd = os.getcwd()
os.chdir(args.inpath) 

my_inputs = []
my_Outputs = []
def read_inputs(input_path):
    with open(input_path, 'r') as f:
        return f.read()
  
for file in os.listdir():
    if file.endswith(".txt"):
        input_path = os.path.join(os.getcwd(),file)
        my_Outputs.append(file)
        my_inputs.append(read_inputs(input_path))




#Accessing English Words
os.chdir(cwd)
eng = args.engDic.read()
eng += "\n" #to include last word
eng_list = []
word = ""
for i in eng:
    if(i == "\n"):
        eng_list.append(word)
        word = ""
    else:
          word += i








#Formatting
uppCase_number = []
punct_number = []
nums_nums = []

abc = ['a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums = ['0','1','2','3','4','5','6','7','8','9']

#Counting Formatting parameters
for y in range(0,len(my_inputs)):
    up = 0
    pun = 0
    num = 0
    w = 0
    ww = 0
    cw = 0
    ell = ""
    for i in my_inputs[y]:
        c = 0
        n = 0
        if (i.isupper()):
            up +=1
        for a in abc:
            if(i == a or i == a.upper()):
                break
            else:
                c += 1 
        for x in nums:
            if(i == x):
                num += 1
                break
            else:
                n +=1

        if (c == 26 and n ==10 and i != " " and i != "\n" and i != "@" and i != "#"):
            pun += 1

        #Checking for ellipsis
        if(i == "."):
            ell +=i
        else:
            ell = ""
        if(ell == "..."):
            pun = pun - 2

    uppCase_number.append(up)
    punct_number.append(pun)
    nums_nums.append(num)



#Removing everything aside from letters
for y in range(0, len(my_inputs)):
    my_inputs[y] = my_inputs[y].lower()
    for i in my_inputs[y]:
        z = 0
        for a in abc:
            if(i != a):
                z +=1
        if(z == 26 and i!= " "):
            my_inputs[y] = my_inputs[y].replace(i,"")






#Splitting Texts from files into lists of words
lists_of_words = []
word = ""

for y in range(0,len(my_inputs)):
    words = []
    for i in my_inputs[y]:
        if(i != " "):
            word += i
            continue
        else:
            if(word != ""):
                words.append(word)
                word = ""

    #To include the last word
    if(word != ""):
        words.append(word)
        word = ""
   
    lists_of_words.append(words)



#SpellChecking
words_number = []
correct_number = []
wrong_number = []

for y in range(0, len(lists_of_words)):
    w = len(lists_of_words[y])
    ww = 0
    cw = 0
    for i in range(0, len(lists_of_words[y])):
        for word in eng_list:
            if(lists_of_words[y][i] == word):
                cw += 1
    words_number.append(w)
    correct_number.append(cw)
    ww = w-cw
    wrong_number.append(ww)





#Generating Output Files Names
#Creating Output Files in the path specified in the 2nd argument
#Overwriting any existing files with same name
os.chdir(cwd)
os.chdir(args.outpath) 

for i in range(0, len(my_Outputs)):
    my_Outputs[i] = my_Outputs[i].replace(".txt","_x74657fa.txt")
    if(os.path.isfile(my_Outputs[i])):
        os.remove(my_Outputs[i])
    o = open(my_Outputs[i], "x")
    o.write("x74657fa\nFormatting ###################\nNumber of upper case letters changed: " + str(uppCase_number[i]) +  
        "\nNumber of punctuations removed: " + str(punct_number[i]) +
        "\nNumber of numbers removed: " + str(nums_nums[i]) + 
        "\nSpellchecking ###################\nNumber of words: " + str(words_number[i]) + 
        "\nNumber of correct words: " + str(correct_number[i]) + 
        "\nNumber of incorrect words: " + str(wrong_number[i]) )




    










