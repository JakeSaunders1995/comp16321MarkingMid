import argparse , os

#Rugby Match Calculator

parser = argparse.ArgumentParser(description='Takes scores from input file and outputs totals in new file')
parser.add_argument('inpath', help="Takes input folder path that contains score files")
parser.add_argument('outpath', help="Saves scores (T1:T2 format) in a new .txt files in the specified path")
args = parser.parse_args()

#Accessing Input Files
cwd = os.getcwd()
os.chdir(args.inpath) 

my_inputs = []
my_Outputs = []
def read_inputs(input_path):
    with open(input_path, 'r') as f:
        return f.read()
  

for file in os.listdir():
    if file.endswith(".txt"):
        input_path = os.path.join(os.getcwd(),file)
        my_Outputs.append(file)
        my_inputs.append(read_inputs(input_path))


#Program

totals=[]
#Replaces new lines with no spaces (if they exist)
for y in range(0,len(my_inputs)):
    my_inputs[y] = my_inputs[y].replace("\n","")
  
    #Team Total Scores
    totT1 = 0
    totT2 = 0

#Calculating points for file(s)

    for i in range(0,len(my_inputs[y]),3):
        team = my_inputs[y][i:i+2]
        points = my_inputs[y][i+2]

        #Determining points based on score
        if(points == "t"):
            points = 5
        elif(points == "d" or points == "p"):
            points = 3
        elif(points == "c"):
            points = 2
        else:
            points = 0


        #Accumulating points for teams
        if(team == "T1"):
            totT1 += points
        elif(team == "T2"):
            totT2 +=points

    #Storing results in T1:T2 Format
    totals.append((str(totT1)+":"+str(totT2)))

#Generating Output Files Names
#Creating Output Files in the path specified in the 2nd argument
#Overwriting any existing files with same name
os.chdir(cwd)
os.chdir(args.outpath) 

for i in range(0, len(my_Outputs)):
    my_Outputs[i] = my_Outputs[i].replace(".txt","_x74657fa.txt")
    if(os.path.isfile(my_Outputs[i])):
        os.remove(my_Outputs[i])
    o = open(my_Outputs[i], "x")
    o.write(totals[i])




    










