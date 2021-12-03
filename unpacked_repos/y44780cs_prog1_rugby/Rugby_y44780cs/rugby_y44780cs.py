import sys
import argparse
import os


args = str(sys.argv[1:])
args = args.replace("[","")
args = args.replace("]","")
args = args.replace(",","")
args = args.replace("'","")


temp=args.split('./')
list_length=len(temp)
list_locations=temp[1:list_length]


location_file_final=""
location_temp=list_locations[0]
for i in range(len(location_temp)):
    element=location_temp[i]
    if element.isspace():
        location_file_final=location_file_final
    else:
        location_file_final=location_file_final+element


location_input="/"+location_file_final



output_folder=list_locations[1]
location_output="/"+list_locations[1]


files = os.listdir(location_input)


list_files_output=[]
list_scores=[]


for yam in range(len(files)):
    doc=location_input+"/"+str(files[yam])
    file_input=open(doc)
    name_length=len(files[yam])
    text=name_length-4
    Output_file_name=files[yam][0:text]
    Output_file_name=location_output+"/"+Output_file_name+"_y44780cs.txt"
    list_files_output.append(Output_file_name)

    
    
    file_read=file_input.read()
    
    list_conversions=file_read.split('T')
    
    team1=[]
    team2=[]
    
    for i in range(len(list_conversions)):
        if '1' in list_conversions[i]:
            team1.append(list_conversions[i])
            
        elif '2' in list_conversions[i]:
            team2.append(list_conversions[i])
    
    
    
    
    score1=0
    score2=0
    
    for score in range(len(team1)):
        if 't' in team1[score]:
            score1=score1+5
        elif 'p' in team1[score]:
            score1=score1+3
        elif 'c' in team1[score]:
            score1=score1+2
        elif 'd' in team1[score]:
            score1=score1+3
        
    
    

    for score in range(len(team2)):
        if 't' in team2[score]:
            score2=score2+5
        elif 'p' in team2[score]:
            score2=score2+3
        elif 'c' in team2[score]:
            score2=score2+2
        elif 'd' in team2[score]:
            score2=score2+3

    points=str(score1)+":"+str(score2)
    list_scores.append(points)
    

for i in range(len(list_files_output)):
    data=list_files_output[i]
    file_open=open(data,'w')
    scores_input=list_scores[i]
    file_open.write(scores_input)
    file_open.close()

    
    