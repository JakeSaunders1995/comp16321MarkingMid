import os.path as path
import sys, os

def read_file(english, input_folder, output_folder):
    if path.isfile(english) and path.isdir(input_folder):
        eng_file = open(english, "r")
        eng_input_list = eng_file.readlines()
        eng_file.close()
        for i in range(len(eng_input_list)-1):
            eng_input_list[i] = eng_input_list[i].strip("\n")

        for file in os.scandir(input_folder):
            inp_file = open(file, "r")
            inp_list = inp_file.readlines()
            print(inp_list)
            inp_file.close()
            output_list = spell_check(eng_input_list, inp_list)
            write_file(output_list, file, output_folder)



def spell_check(english, inp_list):#
    print("SPELL CHECK RAN")
    cl = 0
    punc = 0
    num = 0
    num_words = 0
    corr_words = 0
    incorr_words = 0
    n_banned_list = ["0","1","2","3","4","5","6","7","8","9"]
    p_banned_list = [".","?","!",",",":",";","-","(",")","{","}","[","]","'",'"']

    for i in range(len(inp_list)):
        print("iterate once")
        print("input list", inp_list[i])
        print("length of input list", len(inp_list[i]))
        inp_str = inp_list[i]
        count = 0
        while count < len(inp_str):
            if inp_str[count] == ".":
                if count+3 <= len(inp_str):
                    if inp_str[count+1] == "." and inp_str[count+2] == ".":
                        punc += 1
                        inp_str = inp_str[:count] + inp_str[count+3:]
                        continue
                    else:
                        print("weird if statement")
                        inp_str = inp_str[:count] + inp_str[count+1:]
                        punc += 1
                        continue

                else:
                    if count <= len(inp_str)-1:
                        print("correct if statement")
                        inp_str = inp_str[:count] + " " +  inp_str[count+1:]
                        punc += 1
                        continue
                    else:
                        print("wrong if statement")
                        inp_str = inp_str[:count]
                    punc += 1
                    if count <= len(inp_str)-1:
                        inp_str = inp_str[:count] + inp_str[count+1:]
                        continue
                    else:
                        inp_str = inp_str[:count]

            elif inp_str[count] in p_banned_list:
                punc += 1
                print("punc found")
                if count <= len(inp_str)-1:
                    inp_str = inp_str[:count] + inp_str[count+1:]
                    continue
                else:
                    inp_str = inp_str[:count]
            elif inp_str[count] in n_banned_list:
                num += 1
                if count <= len(inp_str)-1:
                    inp_str = inp_str[:count] + inp_str[count+1:]
                    continue
                else:
                    inp_str = inp_str[:count]
            else:
                lowercase = inp_str[count]
                if inp_str[count] != lowercase.lower() and count <= len(inp_str):
                    print("cl if")
                    cl += 1
                    inp_str = inp_str[:count] + lowercase.lower() + inp_str[count+1:]
                    print(count)

            count += 1
            inp_list[i] = inp_str
        word_list = inp_list[i].split()
        num_words += len(word_list)
        for word in word_list:
            if word in english:
                corr_words += 1
            else:
                incorr_words += 1
    final_string = "\n".join(inp_list)
    print(final_string)
    return [final_string, num_words, corr_words, incorr_words, cl, punc, num]

def write_file(out_list, file, out_path):
    output_file = open(path.join(out_path, path.basename(file)[:-4]+"_s65422mt.txt"), "a")
    output_file.write("s65422mt \n")
    output_file.write("Formatting ################### \n")
    output_file.write("Number of upper case letters changed: " + str(out_list[4]) + "\n")
    output_file.write("Number of punctuations removed: " + str(out_list[5]) + "\n")
    output_file.write("Number of numbers removed: " + str(out_list[6]) + "\n")
    output_file.write("Spellchecking ################### \n")
    output_file.write("Number of words: " + str(out_list[1]) + "\n")
    output_file.write("Number of correct words: " + str(out_list[2]) + "\n")
    output_file.write("Number of incorrect words: " + str(out_list[3]) + "\n")
    output_file.close()


def main():
    try:
        english = sys.argv[1]
        input_folder = sys.argv[2]
        output_folder = sys.argv[3]
    except:
        print("problem reading inputs: check all arguments present. exiting...")
        sys.exit()
    read_file(english, input_folder, output_folder)


if __name__ == "__main__":
    main()
