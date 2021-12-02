import os, argparse, re, string

parser = argparse.ArgumentParser()
parser.add_argument("english", type=open)
parser.add_argument("inputpath", type=str, help= "paste path to inout files")
parser.add_argument("outputpath", type=str, help= "paste path to output files")

originalpath = os.getcwd()

args = parser.parse_args()
path = args.inputpath
output_path = args.outputpath
os.chdir(args.inputpath)
cwd = os.getcwd()



input_file_names = os.listdir()






txt = ".txt"
counter = 0
list_of_files = []
for n in range(len(input_file_names)):
    if re.search(txt, input_file_names[n]):
        counter += 1
        list_of_files.append(input_file_names[n])
        #print(input_file_names[n])
        #print(type(input_file_names[n]))
        x = open(str(input_file_names[n]), "r").readlines()
        #print(x)

for n in range(len(input_file_names)):
    input_file_names[n] = re.split(r'\.txt', input_file_names[n])
    #print(input_file_names[n])
uc_changed = []
punc = []
num_num = []
num_words = []
c_words = []
i_words = []
#print(counter)
#print(list_of_files)
english_words = str(args.english.read().splitlines())
#print(english_words)
#english_wordss = []
#for temp in english_words:
    #temp1 = temp + "\n"
    #english_wordss.append(temp1)
#print(english_wordss)
#print(list_of_files)
list_of_files.sort()
#print(list_of_files)
for n1 in list_of_files:
    print("y45718mk")
    print("Formatting ###################")
    open_file = open(n1, "r").readlines()
    #print(open_file)
    eachone = list(open_file[0])
    #print(eachone)
    count = []
    num = 0
    for temp in eachone:
        if temp.isupper():
            y = temp.replace(temp, temp.lower())
            count += y
            num += 1
        else:
            count += temp
    print("Number of upper case words changed:", num)
    uc_changed.append(num)
    digits = []
    num_digits = 0
    for temp in count:
        if temp.isdigit():
            remove = temp.replace(temp, "")
            digits += remove
            num_digits += 1
        else:
            digits += temp
    string2 = "".join([str(temp) for temp in digits])
    #print(string2)
    count2 = 0
    for temp in string2:
        if temp in ("?", ".", ";", ":", "!", ",", "_", "-", "[", "]", "{", "}", "(", ")", "'", "...", """ " """ ):
            q = string2.index(temp)
            remove2 = string2.replace(temp, "")
            count2 += 1
        else:
            count2 += 0
    #print(remove2)
    print("Number of punctuations removed:", count2)
    punc.append(count2)
    print("Number of numbers removed:", num_digits)
    num_num.append(num_digits)
    print("Spellchecking ###################")
    count4 = 0
    count3 = 0
    final_string2 = remove2.translate(str.maketrans('', '', string.punctuation))
    word_count = final_string2.split()
    #print(word_count)
    #print(final_string2)
    number_of_words = len(word_count)
    print("Number of words:", number_of_words)
    num_words.append(number_of_words)

    for temp in word_count:
        temp1 = "'" + temp + "'"
        if english_words.count(temp1) != 0:
            count4 += 1

        else:
            count3 += 1
            #print(temp1)
    print("Number of correct words:", count4)
    c_words.append(count4)
    print("Number of incorrect words:", count3)
    i_words.append(count3)
    #print(english_words)
name = []
for i in list_of_files:
    #print(i)
    for ii in i:
        if ii == ".":
            index = i.index(".")
            #print(index)
            name.append(i[0:index])
            break
#print(name)

for i in range(len(list_of_files)):
    filename = name[i] + "_y45718mk"+ ".txt"
    outfile = open(filename, "w")
    outfile.write("y45718mk")
    outfile.write("\n")
    outfile.write("Formatting ###################")
    outfile.write("\n")
    outfile.write("Number of upper case letters changed: ")
    outfile.write(str(uc_changed[i]))
    outfile.write("\n")
    outfile.write("Number of punctuations removed: ")
    outfile.write(str(punc[i]))
    outfile.write("\n")
    outfile.write("Number of numbers removed: ")
    outfile.write(str(num_num[i]))
    outfile.write("\n")
    outfile.write("Spellchecking ###################")
    outfile.write("\n")
    outfile.write("Number of words: ")
    outfile.write(str(num_words[i]))
    outfile.write("\n")
    outfile.write("Number of correct words: ")
    outfile.write(str(c_words[i]))
    outfile.write("\n")
    outfile.write("Number of incorrect words: ")
    outfile.write(str(i_words[i]))

    outfile.close()


#filedata = {filename: open(filename, 'r') for filename in blah}
