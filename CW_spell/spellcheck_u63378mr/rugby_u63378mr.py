import sys
import argparse
import os


args = str(sys.argv[1:])
args = args.replace("[","")
args = args.replace("]","")
args = args.replace(",","")
args = args.replace("'","")


Temp_List=args.split('./')
Length_of_List=len(Temp_List)
Locations_List=Temp_List[1:Length_of_List]


Final_Input_Location=""
Temp_Location=Locations_List[0]
for i in range(len(Temp_Location)):
    letter=Temp_Location[i]
    if letter.isspace():
        Final_Input_Location=Final_Input_Location
    else:
        Final_Input_Location=Final_Input_Location+letter


Input_Location="/"+Final_Input_Location




Output_Folder=Locations_List[1]
Output_Location="/"+Locations_List[1]


all_files = os.listdir(Input_Location)


Output_Files_List=[]
Scores_List=[]


for counter in range(len(all_files)):
    file=Input_Location+"/"+str(all_files[counter])
    Input_File=open(file)
    len_of_name=len(all_files[counter])
    copy_text=len_of_name-4
    Output_file_name=all_files[counter][0:copy_text]
    Output_file_name=Output_Location+"/"+Output_file_name+"_u63378mr.txt"
    Output_Files_List.append(Output_file_name)

    
    
    Read_File=Input_File.read()
    
    Convert_Into_List=Read_File.split('T')
    
    Team_1=[]
    Team_2=[]
    
    for length in range(len(Convert_Into_List)):
        if '1' in Convert_Into_List[length]:
            Team_1.append(Convert_Into_List[length])
            
        elif '2' in Convert_Into_List[length]:
            Team_2.append(Convert_Into_List[length])
    
    
    
    
    score_1=0
    score_2=0
    
    
    for point in range(len(Team_1)):
        if 't' in Team_1[point]:
            score_1=score_1+5
        elif 'p' in Team_1[point]:
            score_1=score_1+3
        elif 'c' in Team_1[point]:
            score_1=score_1+2
        elif 'd' in Team_1[point]:
            score_1=score_1+3
        
    
    

    for point in range(len(Team_2)):
        if 't' in Team_2[point]:
            score_2=score_2+5
        elif 'p' in Team_2[point]:
            score_2=score_2+3
        elif 'c' in Team_2[point]:
            score_2=score_2+2
        elif 'd' in Team_2[point]:
            score_2=score_2+3

    Score=str(score_1)+":"+str(score_2)
    Scores_List.append(Score)
    

for i in range(len(Output_Files_List)):
    file_name=Output_Files_List[i]
    Open_file=open(file_name,'w')
    input_score=Scores_List[i]
    Open_file.write(input_score)
    Open_file.close()

    
    