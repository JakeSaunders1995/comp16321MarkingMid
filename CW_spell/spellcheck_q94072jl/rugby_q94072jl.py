
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


    #Reads scores in text file 'Inp'
    with open(Inp, 'r') as finput:
        content = finput.read()
    
    #Teamscore declared as 0    
    T1 = 0
    T2 = 0

    #Set which team will get score
    team = 0

    #Loops until index is greater than length of content in input text file
    i = 0
    while i < len(content):

        #Set team for which score is added to
        if content[i] == "1":
            team = 1
            
        elif content[i] == "2":
            team = 2

        #Addes score depending on type of point
        if team == 1:
            if content[i] == "t":
                T1 = T1 + 5
            elif content[i] == "c":
                T1 = T1 + 2
            elif content[i] == "p":
                T1 = T1 + 3
            elif content[i] == "d":
                T1 = T1 + 3

        elif team == 2:
            if content[i] == "t":
                T2 = T2 + 5
            elif content[i] == "c":
                T2 = T2 + 2
            elif content[i] == "p":
                T2 = T2 + 3
            elif content[i] == "d":
                T2 = T2 + 3    

        #Index increased    
        i = i + 1

    #States which team won and by what score
    winner = ""
    if T1 > T2:
        #print("Team 1 is the winner with final score of " + str(T1) + ":" + str(T2))
        winner = "Team 1"
    elif T2 > T1:
        #print("Team 2 is the winner with final score of " + str(T2) + ":" + str(T1))
        winner = "Team 2"
    else:
        winner = "Draw"
        #print("Both teams draw with final score of " + str(T2) + ":" + str(T1))
        
    ####not sure if this is needed above as instructions only state to output text file
        #however it also states that you should compare scores to determine a winner

    #Writes scores in new Text File 'Out'
    with open(Out, 'w') as foutput:
        foutput.write(str(T1) + ":" + str(T2))


def GetFileName():    
    fileNames = os.listdir(args.FInput) #gets all file names in inputted folderpath
    for fileName in fileNames: #for each file run loop              
        InputFileName = (fileName) #gets name of file to be read
        InputFilePath = (os.path.abspath(os.path.join(args.FInput, InputFileName))) #joins file to input folder path

        OutputNames = (os.path.splitext(fileName)) #splits file name and .txt apart
        OutputFileName = '_q94072jl'.join(OutputNames) #adds my username at the end of the file name
        
        OutputFilePath = (os.path.abspath(os.path.join(args.FOutput, OutputFileName))) #joins file name to output folder path



        main(InputFilePath, OutputFilePath) #run main program while passing input and output file paths



        
        #Logic(InputFileName, OutputFileName)

GetFileName()




