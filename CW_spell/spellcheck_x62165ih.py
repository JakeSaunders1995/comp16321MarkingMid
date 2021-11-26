import argparse
import re
import os 
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dictionary' , type = str, help = "English Word Base")
    parser.add_argument('input' , type = str, help = "Your input file path to be processed.")
    parser.add_argument('output' , type = str, help = "The output folder path where the processed data will be stored in.")
    args = parser.parse_args()
    return str(args.dictionary),str(args.input), str(args.output)
def format(text):
    upperTolower = len(re.findall("[A-Z]", text))
    numeric = len(re.findall("[0-9]",text))
    nonAlpha = text.count("...")
    text = text.replace("...","")
    nonAlpha += len(re.findall("[^\w\d\s]",text))  
    text = text.lower()
    text = re.sub("[0-9]","",text)
    text = re.sub("[^\w\d\s]","",text)

    return [text,"Formatting ###################\nNumber of upper case words transformed: {}\nNumber of punctuation's removed: {}\nNumber of numbers removed: {}\n".format(upperTolower,nonAlpha,numeric)]
def spellcheck(text,dictionary):
    incorrect = 0
    text_list = text.split()

    with open (dictionary,'r') as d:
        d = d.read()
        for word in text_list:
            if not (re.search(r'\b'+ re.escape(word) + r'\b', d)):
                incorrect+=1
                
        
        
    return "Spellchecking ###################\nNumber of words in file: {}\nNumber of correct words in file: {}\nNumber of incorrect words in file: {}\n".format(len(text_list),len(text_list)-incorrect,incorrect)


def main():
    # Retreive Data
    dictionary , inputFolder , outputFolder = parser()
    #Read Data
    txt_arr = sorted([x for x in os.listdir(inputFolder) if x.endswith(".txt")])
    for inputFile in txt_arr:
        with open (os.path.join(inputFolder,inputFile),'r') as data:
            data = data.read()
        
        #Format Data
        formatedData = format(data)
        #SpellCheck
        
        spellstats = spellcheck(formatedData[0],dictionary)
        #Output 
        with open(os.path.join(outputFolder,inputFile.split(".")[0]+"_x62165ih.txt"),'w') as out:
            string = "x62165ih\n{}{}".format(formatedData[1],spellstats)
            out.write(string)
if __name__ == '__main__':
    main()