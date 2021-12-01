import sys
import os

def calcpoints(input_file,output_folder,txtfile):
    team1=0
    team2=0
    t=5
    c=2
    p=3
    d=3

    f_in=open(input_file,"r")
    for aline in f_in:
        for i in range(len(aline)):
            if aline[i].islower():
                if aline[i-1]=='1':
                    if aline[i]=='t':
                        team1+=t

                    elif aline[i]=='c':
                        team1+=c

                    elif aline[i]=='p':
                        team1+=p

                    else:
                        team1+=d
                
                else:
                    if aline[i]=='t':
                        team2+=t

                    elif aline[i]=='c':
                        team2+=c

                    elif aline[i]=='p':
                        team2+=p

                    else:
                        team2+=d
    f_in.close()

    if team2>team1:
        result="team 2 wins"
    elif team2==team1:
        result="draw"
    else:
        result="team 1 wins"

    output_file=output_folder+"/"+txtfile[:-4]+"_s63644vb.txt"

    f_out=open(output_file,"w")
    f_out.write(str(team1)+":"+str(team2))
    f_out.close()


arg_list=(sys.argv)

input_folder= arg_list[1]
output_folder= arg_list[2]
parent_path=os.getcwd()
os.chdir(input_folder)
for txtfile in os.listdir():
    if txtfile.endswith(".txt"):
        os.chdir(parent_path)
        input_file=f"{input_folder}/{txtfile}"
        calcpoints(input_file,output_folder,txtfile)
