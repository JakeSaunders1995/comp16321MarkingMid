import argparse
import os


c = 1 # output in filename(n) in the loop


name = os.getlogin()
parser = argparse.ArgumentParser()
parser.add_argument('dict')
parser.add_argument('folder1')
parser.add_argument('folder2')
args = parser.parse_args()

dict_words = []
with open(args.dict) as f:
    for line in f:
        dict_words.append(line.rstrip())

folder_1 = args.folder1
folder_2 = args.folder2
a = os.listdir(folder_1)
a.sort(key = lambda x:int(x[-5:-4]))
os.chdir(folder_1)
for i in a:
    file = open(i, 'r')
    text = file.readline()

    uppercase = 0
    punctuation = 0
    numbers = 0
    words_number = 0
    correct = 0
    incorrect = 0

    new_text = ""
    new_text_list = text.split(" ")
    # print(new_text_list)
    for n in range(len(new_text_list)):
        for char in new_text_list[n]:
            if ((ord(char) >= 97 and ord(char) <= 122)):
                new_text += char
            elif ((ord(char) >= 65 and ord(char) <= 90)):
                uppercase += 1
                lower_char = ord(char) + 32
                new_text += chr(lower_char)
            elif (ord(char) >= 48 and ord(char) <= 57):
                numbers += 1
                # continue
            elif (char == "\n"):
                continue
            else:
                punctuation += 1

        if ("..." in new_text_list[n]):
            punctuation = punctuation - 2
                # continue
        new_text = new_text + " "
    # print(new_text)


    check_list = new_text.split(" ")
    # print(check_list)
    new_check_list = []
    for item in check_list:
        if item == "":
            continue
        else:
            new_check_list.append(item)

    # print(new_check_list)
    # print(dict_words)

    for word in new_check_list:
        words_number += 1
        if word in dict_words:
            correct += 1
        else:
            # print(word)
            incorrect += 1


    print(name)
    print("Formatting ###################")
    print("Number of upper case words changed: " + str(uppercase))
    print("Number of punctuations removed: " + str(punctuation))
    print("Number of numbers removed: " + str(numbers))
    print("Spellchecking ###################")
    print("Number of words: " + str(words_number))
    print("Number of correct words: " + str(correct))
    print("Number of incorrect words: " + str(incorrect))

    pardir = os.path.abspath(os.path.join(os.path.dirname(folder_1),os.path.pardir))
    # print(os.listdir(pardir))
    # b = os.listdir(folder_2)
    os.chdir(pardir)
    os.chdir(folder_2)
    f = open(("%s%d_m50747jh.txt") %(i[:-5], c), "w+")
    f.write(name + "\n" + 
            "Formatting ###################" + "\n" + 
            "Number of upper case words changed: " + str(uppercase) + "\n" + 
            "Number of punctuations removed: " + str(punctuation) + "\n" + 
            "Number of numbers removed: " + str(numbers) + "\n" + 
            "Spellchecking ###################" + "\n" + 
            "Number of words: " + str(words_number) + "\n" + 
            "Number of correct words: " + str(correct) + "\n" + 
            "Number of incorrect words: " + str(incorrect))
    f.close()
    c += 1

    pardir2 = os.path.abspath(os.path.join(os.path.dirname(folder_2),os.path.pardir))
    # print(pardir2)
    os.chdir(pardir2)
    os.chdir(folder_1)

