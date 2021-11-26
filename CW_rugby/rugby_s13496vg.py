 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 22:50:47 2021

@author: csimage
"""
import sys
import argparse
import os
args = str(sys.argv[1:])
args = args.replace("[","")
args = args.replace("]","")
args = args.replace(",","")
args = args.replace("'","")
print(args,type(args))

Temp_List=args.split('./')
Length_of_List=len(Temp_List)
Locations_List=Temp_List[1:Length_of_List]
print(Locations_List)

Final_Input_Location=""
Temp_Location=Locations_List[0]
for i in range(len(Temp_Location)):
	letter=Temp_Location[i]
	if letter.isspace():
		Final_Input_Location=Final_Input_Location
	else:
		Final_Input_Location=Final_Input_Location+letter


 
Input_Location="/"+Final_Input_Location
all_files = os.listdir(Input_Location)



Output_Folder=Locations_List[1]
Output_Location="/"+Output_Folder 
all_files_output=os.listdir(Output_Location)
 

sc=""
score=[] 
allfiles=os.listdir(Input_Location)
 
output_files=[]
for i in range(len(allfiles)):
    file=Input_Location+"/"+str(allfiles[i])
    name=str(allfiles[i])
    length=len(name)
    temp_name=name[0:length-4]
    perm_name=temp_name+"_[s13496vg].txt"
    output_files.append(perm_name)
    
    


    Read=open(file)
    form=Read.read()
    
    T1=[]
    T2=[]
    T=[] 
    s1=0
    s2=0
    for i in range(len(form)):
         T.append(form[i])
    
    for i in range(len(T)):
        if T[i]=="1":
            T1.append(T[i+1])
        elif T[i]=="2":
            T2.append(T[i+1])
     
            
    for v in T1:
        if v == "t":
            s1=s1+5
        elif v== "c":
            s1=s1+2
        elif v== "P":
            s1=s1+3
        else:
            s1=s1+3
        
    for v in T2:
        if v == "t":
            s2=s2+5
        elif v== "c":
            s2=s2+2
        elif v== "P":
            s2=s2+3
        else:
            s2=s2+3      
             
    if s1>s2:
        sn="Team 1 Wins!"
    elif s2>s1:
        sn="Team 2 Wins!"
    else:
        sn="Its A Draw!"
        
    sc=str(s1)+":"+str(s2)
    score.append(sc)
     

 
for i in range(len(allfiles)):
    fname= Output_Location+'/'+output_files[i]     
    outf=open(fname,"w")      
    # outf.write(result[i])
    # outf.write("\n")
    outf.write(score[i])
    outf.close()

