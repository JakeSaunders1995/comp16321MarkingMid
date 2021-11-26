import sys, os

filenames = os.listdir(sys.argv[2])
with open(sys.argv[1]) as f:
    english_words = [i.replace('\n', '') for i in f.readlines()]

for input_file in filenames:
    with open(sys.argv[2] + "/" + input_file) as f:
        s = f.read()

    s = s.replace('\n', ' ')
    nums = 0
    digits = "1234567890"
    for i in digits:
        nums += s.count(i)
        s = s.replace(i, '')

    puncs = 0
    punctuation = "... . ? ! , : ; - – ( ) [ ] { } ' \"".split(' ')
    for i in punctuation:
        puncs += s.count(i)
        s = s.replace(i, '')

    uppers = 0
    for i in s:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            uppers += 1

    s = s.lower()

    words = s.split(' ')
    new_words = []
    for i in words:
        if i not in ["\n", "", " "]:
            new_words.append(i)
    words = new_words

    print(input_file + ": " + "\n\n")
    print(words)
    correct = 0
    for i in words:
        if i.lower() in english_words:
            correct += 1


    output = "k01756ws\n"

    output += "Formatting ###################\n"
    output += "Number of upper case letters changed: " + str(uppers) + "\n"
    output += "Number of punctuations removed: " + str(puncs) + "\n"
    output += "Number of numbers removed: " + str(nums) + "\n"
    output += "Spellchecking ###################\n"
    output += "Number of words: " + str(len(words)) + "\n"
    output += "Number of correct words: " + str(correct) + "\n"
    output += "Number of incorrect words: " + str(len(words) - correct)

    output_filename = sys.argv[3] + "/" + input_file[:-4] + "_k01756ws.txt"

    with open(output_filename, 'w') as f:
        f.write(output)
