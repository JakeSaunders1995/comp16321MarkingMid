import string

import argparse
import os

##Starts the parser
parser = argparse.ArgumentParser()

##Declaring parameters in argparse
parser.add_argument("Dictionary", help = "Text file containing English Words, use """)
parser.add_argument("FInput", help = "Folder path containing Text Files of passages, use """)
parser.add_argument("FOutput", help = "Folder path where Text Files of spellchecked passages are stored in, use """)

##declarin args.variable to be used in program
args = parser.parse_args()


def readDictionaryFile(DictionaryFilename): #Reads Dictionary file
    

    dictionaryWords = [] #Declaers dictionaryWords as a list

    DictionaryFile = open(DictionaryFilename, "r") #Opens DictionFilename as DictionaryFile

    for line in DictionaryFile: 
        word = line.strip()
        dictionaryWords.append(word) #For each line in file, adds to list

    DictionaryFile.close() #Close file
      
    return dictionaryWords #return list of correct dictionary words
    
def readTextFile(InputTextFileName): #Reads Inputted text file and removes punctuation, digits and uppercase
    

    words = [] #Declares words as list
    inputFile = open(InputTextFileName, "r") #Opens InputTextFileName as inputFile
    for line in inputFile:
        wordsOnLine = line.strip().split() #all words on line remove all spaces imbetween and after words
        for word in wordsOnLine:
            Exempt = string.digits + string.punctuation
            words.append(word.strip().strip(Exempt).lower()) #For each word, remove any numbers, punctuation and convert to lowercase before adding to list
            
    inputFile.close() #close file

    words = ' '.join(words).split() #remove any missed punctuation     
        
    return words  


    

def findErrors(dictionaryWords, textWords): #Checks for any incorrect and correct spelt words
    misspelledWords = [] 
    correctWords = [] #declares misspelledWords and correctWords as list
    for word in textWords: #for each word in text file run loop       
        if word not in dictionaryWords:  #if current word does not exist in dictionaryWords (it means its misspelt) add to misspelledWords
            misspelledWords.append(word)
        else:   #Otherwise, word is correctly spelled, so add to correctWords 
            correctWords.append(word)

    

    NumberOfMisspelledWords = str(len(misspelledWords)) #get number of misspelled words (elements) in misspelledWords and convert to string    

    NumberOfCorrectWords = str(len(correctWords)) #get number of correctly words (elements) in correctWords and convert to string
    
    NumberOfWords = str(len(textWords)) #get number of words (elements) in textWords and convert to string
            
    return NumberOfMisspelledWords, NumberOfCorrectWords, NumberOfWords

def writeErrors(OutputTextFileName, NumberOfMisspelledWords, NumberOfCorrectWords, NumberOfWords, NumberOfUppercase, NumberOfDigits, NumberOfPuncuation): #Write all data needed for output File



    with open(OutputTextFileName, 'w') as foutput: #Open OutputTextFileName as foutput
        
        
        print("q94072jl", file = foutput)
        print("Formatting ###################", file = foutput)
        print("Number of upper case letters changed: " + NumberOfUppercase , file = foutput)
        print("Number of punctuations removed: " + NumberOfPuncuation, file = foutput)
        print("Number of numbers removed: " + NumberOfDigits, file = foutput)
        print("Spellchecking ###################", file = foutput)
        print("Number of words: " + NumberOfWords, file = foutput)        
        print("Number of correct words: " + NumberOfCorrectWords, file = foutput)
        print("Number of incorrect words: " + NumberOfMisspelledWords, file = foutput)

        ##print final spellcheck to text document (could also use foutput.write("\n") however, this seemed more simpler and concise)

def getInfo(Inp): #read TextFile however retaining all punctuation, uppercase and digits
    with open(Inp, "r") as finp: #Open file Inp as finp

        content = finp.read()
        content = content.split()
        content = ''.join(content) #read all text in textfile and remove any spaces


    return content


def Uppercase(Inp): #counts number of uppercase letters
    Ualpha = string.ascii_uppercase #define uppercase alphabet using import string
    NumOfUp=0
    for letter in Inp:
        if Inp[(Inp.index(letter))] in Ualpha:
            NumOfUp += 1
    #for each number of Uppercase letters in text file, NumOfUp increases by 1
    return str(NumOfUp)




def Numbers(Inp): #counts number of digits 
    Digits = string.digits #define digits alphabet using import string
    NumOfNums=0
    for element in Inp:
        if Inp[(Inp.index(element))] in Digits:
            NumOfNums +=1
    #for each number of digits, increase NumOfNums by 1
    return str(NumOfNums)




def Punct(Inp): #counts number punctuation
    Punctuation = string.punctuation #define punctuation alphabet using import string
    NumOfPunct=0
    for element in Inp:
        if Inp[(Inp.index(element))] in Punctuation:
            NumOfPunct +=1
    #for each punctuation, increase NumOfPunct by 1
    return str(NumOfPunct)




def main(InputFilePath, OutputFilePath):

    DictionaryFile = args.Dictionary #DictionaryFile is set to path (.\.txt) inputted by user
    InputFile = InputFilePath   #see GetFileName()
    OutputFile = OutputFilePath    #see GetFileName()

    DictionaryList = readDictionaryFile(DictionaryFile) #DictionaryList contains list of words from dictionary file    
    textList = readTextFile(InputFile) #textList contains list of words from inputted text file and removes digits, punctuation and uppercase

    content = getInfo(InputFile) #content contains list of words from inputted text file with digits, punctuation and uppercase
    NumberOfUppercase = Uppercase(content) #number of uppercase letters as string (from function)
    NumberOfDigits = Numbers(content) #number of digits as string (from function)
    NumberOfPuncuation = Punct(content) #number of punctuation as string (from function)
    
    
   
    wordList = findErrors(DictionaryList, textList) #Gets number of words, misspeltwords and correct words
    writeErrors(OutputFile, wordList[0], wordList[1], wordList[2], NumberOfUppercase, NumberOfDigits, NumberOfPuncuation) #passes all relavent data to be written in writeErrors function



    
def GetFileName():    
    fileNames = os.listdir(args.FInput) #gets all file names in inputted folderpath
    for fileName in fileNames: #for each file run loop              
        InputFileName = (fileName) #gets name of file to be read
        InputFilePath = (os.path.abspath(os.path.join(args.FInput, InputFileName))) #joins file to input folder path

        OutputNames = (os.path.splitext(fileName)) #splits file name and .txt apart
        OutputFileName = '_q94072jl'.join(OutputNames) #adds my username at the end of the file name
        
        OutputFilePath = (os.path.abspath(os.path.join(args.FOutput, OutputFileName))) #joins file name to output folder path


        



        main(InputFilePath, OutputFilePath) #run main program while passing input and output file paths



GetFileName()

















