import argparse
import os
import re
import sys

def rugby(input_file,output_file):

    src_data = input_file.readline()
    #print(src_data)

    t1_points = 0
    t2_points = 0
    
    for i in range(0,len(src_data),3):
        item = src_data[i:i+3]
        points = 0   
        points_tag = item[2:3]
        team_tag = item[0:2]
        if points_tag == 't':
            points = 5
        elif points_tag == 'c':
            points = 2
        elif points_tag == 'p':
            points = 3
        elif points_tag == 'd':
            points = 3
        else:
            pass
        
        if(team_tag == 'T1'):
            t1_points = t1_points +  points
        elif(team_tag == 'T2'):
            t2_points = t2_points +  points
        else:
            pass        
        #print(points_tag,points,team_tag)
        
    result = str(t1_points) + ":" +str(t2_points)
    #print(result)
    output_file.write(result)


user_name = "w80290jl"
input_folder = sys.argv[1]
output_folder = sys.argv[2]

if output_folder.endswith('\\') or output_folder.endswith('/'):
    pass
else:
    output_folder = output_folder +"/"

#print("input_folder:",input_folder)
#print("output_folder:",output_folder)

for root, dirs, files in os.walk(input_folder):
    for f in files:
        input_file_path = os.path.join(root, f)        
        input_file = open(input_file_path,'r')
        
        output_file_name = f.split('.')[0]+"_"+user_name+".txt"
        output_file_path = output_folder + output_file_name
        output_file = open(output_file_path,'w')
        rugby(input_file,output_file)
        input_file.close()
        output_file.close()