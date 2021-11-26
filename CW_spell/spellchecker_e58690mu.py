import os, sys, string

for filename in os.listdir(sys.argv[2]):
        with open(os.path.join(sys.argv[2], filename)) as f:
            if filename.endswith(".txt"):
                text = f.read()
                f.close()
                path = sys.argv[1]
                d = open(os.path.join(path), 'r')
                dictionary = d.read().split()
                d.close()
                punctuationCount = 0
                punctuation = string.punctuation
                punctuationCounted = 0
                numberCount = 0
                numberCounted = 0
                capitalCount = 0
                capitalCounted = 0
                count=0
                while count < len(text):
                    if text[count].isdigit():
                        numberCounted += text.count(text[count])
                        text = text.replace(text[count], " ")
                        numberCount += 1
                    for i in text[count]:
                        if i in string.ascii_uppercase:
                            capitalCounted += text.count(text[count])
                            text = text.replace(text[count], text[count].lower())
                            capitalCount+=1
                        if i in string.punctuation:
                            punctuationCounted += text.count(text[count])
                            text = text.replace(text[count], "")
                            punctuationCount+=1
                    count+=1
                incorrectwords = 0
                correctwords = 0
                length = len(text.split())
                for i in text.split():
                    if i not in dictionary:
                        incorrectwords+=1
                    else:
                        correctwords+=1
                filename = filename[:-4]
                path = sys.argv[3]
                f = open(os.path.join(path, filename + "_e58690mu.txt"), 'w')
                f.write("e58690mu\n")
                f.write(f"Formatting ###################\n")
                f.write(f"Number of upper case letters changed: {str(capitalCounted)}\n")
                f.write(f"Number of punctuations removed: {str(punctuationCounted)}\n")
                f.write(f"Number of numbers removed: {str(numberCounted)}\n")
                f.write(f"Spellchecking ###################\n")
                f.write(f"Number of words: {length}\n")
                f.write(f"Number of correct words: {correctwords}\n")
                f.write(f"Number of incorrectwords: {incorrectwords}")
            else:
                continue
