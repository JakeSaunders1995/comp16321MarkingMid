#import modules
import argparse
import os
#arguments
parser = argparse.ArgumentParser()
parser.add_argument("input", help="The input filepath")
parser.add_argument("output", help="The output filepath")
input_output=parser.parse_args()
input_file=input_output.input
output_file=input_output.output
files = os.listdir(input_file)




#functions
def find_points(type):
    if type=="t":
        return 5
    elif type=="c":
        return 2
    elif type=="p":
        return 3
    elif type=="d":
        return 3
#start of main program

#iteration of all possible file
for file in files:
    file_path=input_file+'/'+file
    scores_file=open(file_path,'r')
    scores=scores_file.read()
    #turns scores into an array
    scores_array=[]
    for i in range(0,(int(len(scores)/3))):
        score_word_temp=""
        for x in range(0,3):
            score_word_temp+=scores[(3*i)+x]
        scores_array.append(score_word_temp)


    #determines scores
    t1_point=0
    t2_point=0
    for b in scores_array:
        if b[1]=="1":
            t1_point+=find_points(b[2])
        elif b[1]=="2":
            t2_point+=find_points(b[2])
#determines winner
    if t1_point>t2_point:
        winner="Team 1"
    elif t2_point>t1_point:
        winner="Team 2"
    else:
        winner="Its a draw"


#outputs scores to files
    scores_file.close()
    score_out_temp=file.rstrip(".txt")
    score_out_filepath=output_file+"/"+score_out_temp+"_j86153jd.txt"
    scores_out_file=open(score_out_filepath,'w')
    scores_out_file.write(str(t1_point)+":"+str(t2_point))
    scores_out_file.close()
