import argparse
import os


    
n = 0

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("eng_words", help="Enter English Word File here")
    parser.add_argument("input_file", help="Enter input folder name")
    parser.add_argument("output_file", help="Enter output folder name")
    args = parser.parse_args()
    wfile = str(args.eng_words)
    wordfile = open(wfile, "r")
    readfile = wordfile.read()
    folder = str(args.input_file)
    outfolder = str(args.output_file)
    files = os.listdir(folder)
    files.sort()
    
    for filename in files:
        file = os.path.join(folder, filename)
        
        openfile = open(file, "r")
        newval = openfile.read()
        num = 0
        pun = 0
        lower = 0
        wordcount = 0
        cwords = 0
        icwords = 0
        list_num = ["0","1","2","3","4","5","6","7","8","9"]
        list_pun = ["'","!","(",")","-","[","]","{","}",";",":",'"',"/",",","."]
        for lines in newval: #Going through each line in the file
            words = lines.split() #Stripping white spaces and making a list of words
            for word in words: #iterating through list of words
                if word in list_num:  #removing numbers
                    newval = newval.replace(word,"")
                    num += 1
                if word in list_pun:  #removing punctuation
                    newval = newval.replace(word,"")
                    pun += 1
                if word.isupper() is True:  #removing capital
                    newval = newval.replace(word,word.lower())
                    lower += 1
        
        wlower = "Number of upper case letters changed: " + str(lower) + "\n"
        wpun = "Number of punctuations removed: " + str(pun) + "\n"
        wnum = "Number of numbers removed: " + str(num) + "\n"


        #Accessing the dictionary file for word check
        newvalsplit = newval.split()
        splitval = readfile.split()
        wordcount = len(newval.split())
        wwordcount = "Number of words: " + str(wordcount) + "\n"

        for new_words in newvalsplit:
            if new_words in splitval:
                cwords += 1
            else:
                icwords += 1

        
        wcwords = "Number of correct words: " + str(cwords) + "\n"
        wicwords = "Number of incorrect words: " + str(icwords) + "\n"
        out_name = files[n]
        out_name = out_name.replace(".txt", "_f06903rd.txt")
        final_out = os.path.join(outfolder, out_name)
        out_open = open(final_out, "w")
        out_open.write("f06903rd\n")
        out_open = open(final_out, "a")
        out_open.write("Formatting ###################\n")
        out_open.write(wlower)
        out_open.write(wpun)
        out_open.write(wnum)
        out_open.write("Spellchecking ###################\n")
        out_open.write(wwordcount)
        out_open.write(wcwords)
        out_open.write(wicwords)
        n += 1