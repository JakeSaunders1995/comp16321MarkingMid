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
 
Text_File_Location="/"
Temp_Location=Locations_List[0]
for i in range(len(Temp_Location)):
	letter=Temp_Location[i]
	if letter.isspace():
		Text_File_Location=Text_File_Location
	else:
		Text_File_Location=Text_File_Location+letter

Final_Input_Location=""
Temp_Location=Locations_List[1]
for i in range(len(Temp_Location)):
	letter=Temp_Location[i]
	if letter.isspace():
		Final_Input_Location=Final_Input_Location
	else:
		Final_Input_Location=Final_Input_Location+letter



Input_Location="/"+Final_Input_Location
all_files = os.listdir(Input_Location)



Output_Folder=Locations_List[2]
Output_Location="/"+Locations_List[2] 
all_files_output=os.listdir(Output_Location) 
UC=[]
PC=[]
NC=[]
TC=[]
CC=[]
IC=[]
allfiles=os.listdir(Input_Location)
print()
for i in range(len(allfiles)):
    file=Input_Location+"/"+str(allfiles[i])
#import string ut_Location+"/"+str(allfiles[i])
    Read=open(file)
    check=Read.read() 

    ncount=0
    pcount=0
    ccount=0
    pos=0
    ind=0
    t=""
    l=len(check)
    A=[]
    B=['!','"','...','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','[',']','^','_','`','{','|','}','~']
    for v in B:              
        for i in range(len(check)):
            if v == check[i]:
                pcount+=1
        check=check.replace(v,"")
    #pcount=l-len(check)
     
    for i in range(10):    
        i=str(i)
        ncount+=check.count(i)
         
    
    for i in range(len(check)):
        if check[i].isdigit():
            check=check.replace(check[i]," ")     
            
           
    A=check.split() 
    for v in A:
        pos=A.index(v)
        for i in range(len(v)):        
            if v[i].isupper():
                ccount+=1
                u=v[i]            
                l=v[i].lower()            
                copy=v.replace(u,l)
                A[pos]=copy           
                                                        
    y=open(Text_File_Location)
    rd=y.read()
    
    words=[] 
    wcount=0
    tcount=len(A)
    words=rd.split()
    
    for k in A:
        if k not in words:
            wcount+=1 
    icount=tcount-wcount
    UC.append(ccount)
    PC.append(pcount)
    NC.append(ncount)
    TC.append(tcount)
    CC.append(icount)
    IC.append(wcount)

for i in range(len(allfiles)): 
    fname=Output_Location+"/test_file"+str(i+1)+"_[s13496vg].txt"
    outf=open(fname,"w")           
    outf.write("[s13496vg]")
    outf.write("\n")
    outf.write("Formatting ###################")
    outf.write("\n")
    outf.write("Number of upper case words transformed:")
    outf.write(str(UC[i]))
    outf.write("\n")
    outf.write("Number of punctuation’s removed:")
    outf.write(str(PC[i]))
    outf.write("\n")
    outf.write("Number of numbers removed:")
    outf.write(str(NC[i]))
    outf.write("\n")
    outf.write("Spellchecking ###################")
    outf.write("\n")
    outf.write("total number of words:")
    outf.write(str(TC[i]))
    outf.write("\n")
    outf.write("Correct words:")
    outf.write(str(IC[i]))
    outf.write("\n")
    outf.write("incorrect words:")
    outf.write(str(CC[i]))
    outf.write("\n")          
    outf.close()    
        

 
    
    
    
        
        
            
        
        
    
     
             
