import argparse,os,re
parser = argparse.ArgumentParser()
parser.add_argument("englishWords")
parser.add_argument("input_dir")
parser.add_argument("output_dir")
args = parser.parse_args()

def spellCheck(sentence):
    numbers = len(re.findall(r"[0-9]", sentence))
    sentence = re.sub(r"[0-9]","", sentence)
    
    symbols = """.?!,:;-—[]'{}"()"""
    punctuation = 0
    for symbol in symbols:
        if symbol in sentence:
            if symbol == "." and "..." in sentence:
                numOfEllipses = sentence.count("...")
                punctuation -= (2*numOfEllipses)
            punctuation += sentence.count(symbol)
            sentence = sentence.replace(symbol,"")               
    
    uppercase = len(re.findall(r"[A-Z]", sentence))
    sentence = sentence.lower()
    
    words = sentence.split()
    numOfWords = len(words)
    correct = 0
    incorrect = 0
    lines = []
    with open(args.englishWords) as file:
        for line in file.readlines():
            lines.append(line.strip())
        for word in words:
            if(word in lines):
                correct += 1
            else:
                incorrect += 1
    return "s68250ma\nFormatting ###################\nNumber of upper case letters changed: "+str(uppercase)+"\nNumber of punctuations removed: "+str(punctuation)+"\nNumber of numbers removed: "+str(numbers)+"\nSpellchecking ###################\nNumber of words: "+str(numOfWords)+"\nNumber of correct words: "+str(correct) + "\nNumber of incorrect words: "+ str(incorrect)
if(os.path.isdir(args.input_dir)):
    for files in os.listdir(args.input_dir):
        inputFile = os.path.join(args.input_dir, files)
        outputFile = os.path.join(args.output_dir,str(files.replace(".txt","_s68250ma.txt")))
        with open(inputFile, 'r') as file:
            with open(outputFile, 'w') as file2:
                file2.write(spellCheck(file.read()))