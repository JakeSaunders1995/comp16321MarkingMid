import sys, os

f_eng = sys.argv[1]
f_in = sys.argv[2]
f_out = sys.argv[3]


for in_f_name in os.listdir(f_in):
    input_file = open(os.path.join(f_in, in_f_name), "r")
    englishWords = open(f_eng, "r")
    correctly_spelled = 0
    incorrectly_spelled = 0
    tot_words = 0
    uc_transform = 0
    rm_punc = 0
    rm_num = 0
    punctuations = [".",",","?","!","{","}","'",'"',"(",")","[","]",":",";","-","…","_"]

    words = englishWords.read().split()
    lines = input_file.readline().split()
    for i in range(len(lines)):
        line = lines[i]
        out_line = ""
        for char in line:
            if char.isalpha() and char.isupper():
                char = char.lower()
                uc_transform += 1
            elif char.isnumeric():
                char = ""
                rm_num += 1
            elif char in punctuations:
                char = ""
                rm_punc += 1
            elif char.isalnum() != True:
                char = ""
            out_line += char
        lines[i] = out_line

    for item in lines:
        if item == "":
            lines.remove(item)

    for i in range(len(lines)):
        if lines[i] in words:
            correctly_spelled += 1
        else:
            incorrectly_spelled += 1
    in_f_name_arr = in_f_name.split(".")
    out_f_name = in_f_name_arr[0] + "_d66835dg." + in_f_name_arr[1]
    try:
        output_file = open(os.path.join(f_out, out_f_name), "w")
    except:
        os.makedirs(f_out)
        out_f_name = in_f_name_arr[0] + "_d66835dg." + in_f_name_arr[1]
        output_file = open(os.path.join(f_out, out_f_name), "w")

    output_message = "d66835dg\nFormatting ###################\nNumber of upper case words changed: "+str(uc_transform)+"\nNumber of punctuations removed: "+str(rm_punc)+"\nNumber of numbers removed: "+str(rm_num)+"\nSpellchecking ###################\nNumber of words: "+str(len(lines))+"\nNumber of correct words: "+str(correctly_spelled)+"\nNumber of incorrect words: "+str(incorrectly_spelled)

    output_file.write(output_message)
