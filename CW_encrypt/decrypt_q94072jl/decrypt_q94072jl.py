import argparse
import os

##Starts the parser
parser = argparse.ArgumentParser()

##Declaring parameters in argparse
parser.add_argument("FInput", help = "Folder path containing Text Files of ruby scores, use """)
parser.add_argument("FOutput", help = "Folder path where Text Files of ruby scores to be stored in, use """)

##declarin args.variable to be used in program
args = parser.parse_args()

def main(Inp, Out):

    ##read file 
    with open(Inp, 'r') as finput: #Opens file Inp as finput 
        Content = finput.read() #Reads file and stores in Content
    SplitContent = Content.split(":") #Content is split with ":" as its splitter
    DecryptionMethod = SplitContent[0]  #First item is copied to DecryptionMethod
    

    InputData = SplitContent[1] #Second item is copied to InputData
   
    ##run code
    if DecryptionMethod == "Morse Code":  #checks if text file is encoded using morse code
        Message = Morse(InputData) 
        
    elif DecryptionMethod == "Caesar Cipher(+3)":  #checks if text file is encoded using caesar cipher
        Message = Caesar(InputData)
            
    elif DecryptionMethod == "Hex": #checks if text file is encoded using hex
        Message = Hex(InputData) 
    ##write
    with open(Out, 'w') as foutput: #Opens file Out as foutput
        foutput.write(Message) #Writes Message to file



def Caesar(sentence):
    import string
    #Loops for number of letters in inputted sentence
    for i in range(len(sentence)):
        #Declares each type of alphabet as strings
        alpha = string.ascii_lowercase
        nums = string.digits
        punct = string.punctuation
        char = alpha + nums + punct #Combines all alphabets together
        Caesar_alpha = alpha[23:] + alpha[:23]  #Declares shifted version(by -3 or 23 for decrypt) of each alphabet
        Caesar_nums = nums[7:] + nums[:7]  #Shifts numbers (by -3 or 7)
        Caesar_punct = punct[29:] + punct[:29]   #shift punctuation by  (-3 or 29)
        Caesar = (Caesar_alpha + Caesar_nums + Caesar_punct)  #Combines all shifted alphabets
        table = str.maketrans(char, Caesar) #Creates table with normal alphabet and shifted alphabet
        decipher = sentence.translate(table)  #Converts sentence using table as reference
        
        
    return str(decipher) #converts to string



def Morse(message):
    #Declare morse code dictionary
    dictionary = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                 '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                 '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                 '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2',
                 '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                 '--...': '7', '---..': '8', '----.': '9', '-----': '0',
                 '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
                 '-....-': '-', '-.--.': '(', '-.--.-': ')', '-.-.--': '!'}
    message += ' ' #adds space to end of message so program recognises character
 
    decipher = ''
    word = ''

    message = message.replace('/', '')  #remove / from input (shown in example file)
    for letter in message:  

        if (letter != ' '): #checks for spaces
            i = 0
            EncodedWord += letter #adds each letter (- or .) to Encoded word if it isn't a space
 
        else: #incase there is a space
            i += 1
            #when there is a space, i increases by 1, and it also means that a new character           
            if i == 2 : #when i = 2, theres 2 spaces, which means new character 
                decipher += ' ' #Adds space to final message to seperate words
            else:
               
                decipher += dictionary[EncodedWord] #Adds translated word to final message
                
                EncodedWord = '' #resets/empties EncodedWord for next word
            decipher = decipher.lower() #makes final message lowercase
 
    return decipher


def Hex(HexInp):

    HexInp = HexInp.replace(' ', '') #remove spaces
    output = ""
    if len(HexInp) % 2 == 0: #checks if its even number of letters (hex come in 2s)
        for i in range(0,len(HexInp), 2):
            subStr = HexInp[i] + HexInp[i+1] 
            output += (chr(int((subStr),16))) #convert to letters

    decipher = (output).lower() 

    return decipher




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









