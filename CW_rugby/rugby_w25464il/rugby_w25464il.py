import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_file_path",help="Path to the input folder")
parser.add_argument("output_file_path",help="Path to the output folder")
args = parser.parse_args()

def main(input_file):
    data = open(args.input_file_path+"/"+input_file,"r").read().rstrip() # strip whitespace
    score = {"T1":0,"T2":0} # dict for scores easy to access
    types = {"t":5,"c":2,"p":3,"d":3} # dict for score types for easy to access; switch/case statement only introduced in 3.10
    for x in range(int(len(data)/3)): # can split input into groups of 3 characters, indicating team and score change
        team = data[3*x:3*x+2]
        scoretype = data[3*x+2]
        score[team]+=types[scoretype]
    
    if score["T1"] == score["T2"]: # result announced
        print("Draw")
    elif score["T1"] > score["T2"]:
        print("Team 1 wins")
    else:
        print("Team 2 wins")
        
    stringtowrite = str(score["T1"])+":"+str(score["T2"])+"\n"
    print("Final score:",stringtowrite)
    try: # write to file
        open(args.output_file_path+"/"+input_file[:-4]+"_w25464il.txt","x").write(stringtowrite)
    except:
        open(args.output_file_path+"/"+input_file[:-4]+"_w25464il.txt","w").write(stringtowrite)


for filename in os.listdir(args.input_file_path):
    main(filename)