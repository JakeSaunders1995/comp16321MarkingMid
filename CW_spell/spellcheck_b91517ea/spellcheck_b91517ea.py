import sys, re, os

for file in os.listdir(sys.argv[2]):
    with open(os.path.join(sys.argv[2], file), 'r') as f:
        file1 = str(f.read())

    englishFile = open(sys.argv[1], "r")
    newFilename = str(os.path.splitext(file)[0]) + "_b91517ea.txt"
    newFile = os.path.join(sys.argv[3], newFilename)
    file2 = open(newFile, "w")

    text = str(file1)
    english = str(englishFile.read())
    new = ""

    uppercase = 0
    punctuation = 0
    number = 0
    correct = 0
    incorrect = 0
    words = 0

    for letter in text:
        if letter.isalpha() == True:
            if letter.isupper():
                uppercase += 1
            new += letter.lower()
        elif letter.isdigit() == True:
            letter += ""
            number += 1
        elif letter == " ":
            new += " "
        elif letter == "\n":
            new += " "
        else:
            letter += ""
            punctuation += 1
    
    punctuation -= text.count("...") * 3
    punctuation += text.count("...")

    for word in new.split():
        words += 1
        if re.search(r"\b" + word + r"\b", english):
            correct += 1
        else:
            incorrect += 1

    print("b91517ea", file=file2)
    print("Formatting ###################", file=file2)
    print("Number of upper case letters changed:", uppercase, file=file2)
    print("Number of punctuations removed:", punctuation, file=file2)
    print("Number of numbers removed:", number, file=file2)
    print("Spellchecking ###################", file=file2)
    print("Number of words:", words, file=file2)
    print("Number of correct words:", correct, file=file2)
    print("Number of incorrect words:", incorrect, file=file2)