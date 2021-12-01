import os, argparse, re, string

parser = argparse.ArgumentParser()
#parser.add_argument("english", type=open)
parser.add_argument("inputpath", type=str, help= "paste path to inout files")
parser.add_argument("outputpath", type=str, help= "paste path to output files")

originalpath = os.getcwd()

args = parser.parse_args()
path = args.inputpath
output_path = args.outputpath
os.chdir(args.inputpath)
cwd = os.getcwd()

score_1 = 0
result = []
score_2 = []
score = []



input_file_names = os.listdir()
txt = ".txt"
counter = 0
list_of_files = []
for n in range(len(input_file_names)):
    if re.search(txt, input_file_names[n]):
        counter += 1
        list_of_files.append(input_file_names[n])
        #print(input_file_names[n])
        #print(type(input_file_names[n]))
        x = open(str(input_file_names[n]), "r").readlines()
        #print(x)
#print(list_of_files)
list_of_files.sort()
#print(list_of_files)

for n1 in list_of_files:
    #print(n1)
    y = open(str(n1), "r").readlines()
    #print(y)
    team_1_score = 0
    team_2_score = 0
    count4 = 0
    while count4 == 0:
        count3 = 0
        while count3 < len(y[0]):
             eachone = list(y[count4][count3:(count3 +3)])
             #print(list1[count4][count3:(count3 +3)])
             #print(eachone)

             if eachone[1] == "1":
                #print("Team one score!")
                if eachone[2] == "t":
                     team_1_score += 5

                elif eachone[2] == "c":
                    team_1_score += 2

                elif eachone[2] == "p" or "d":
                    team_1_score += 3

             if eachone[1] == "2":
                #print("Team two score!")
                if eachone[2] == "t":
                        team_2_score += 5
                elif eachone[2] == "c":
                        team_2_score += 2
                elif eachone[2] == "p" or "d":
                        team_2_score += 3

             count3 += 3
        count4 += 1
    total = []
    if team_1_score > team_2_score:
        #print("The winner is Team 1")
        result.append("The winner is Team 1")
        total = str(team_1_score) + ":" + str(team_2_score)
        score.append(total)
    elif team_1_score == team_2_score:
        #print("This is a draw!")
        result.append("This is a draw!")
        total = str(team_1_score) + ":" + str(team_2_score)
        score.append(total)
    else:
        #print("Team 2 is victorious!")
        result.append("Team 2 is victorious!")
        total += str(team_1_score) + ":" + str(team_2_score)
        score.append(total)
    #print(result)
    #print(str(team_1_score) + ":" + str(team_2_score))
    #total = str(team_1_score) + ":" + str(team_2_score)
    #score.append(total)
    #print(len(score))
    #print(type(score))
    #print(score[0])
    #sscore = score[0]
    #s = "".join(sscore)
    #print(s)
    #score[0] = s
count = []
for n2 in score:
    s =  "".join(n2)
    count.append(s)
print(count)
name = []
#print(list_of_files)
for i in list_of_files:
    #print(i)
    for ii in i:
        if ii == ".":
            index = i.index(".")
            #print(index)
            name.append(i[0:index])
            break
    #print(name)
for i in range(0, len(list_of_files)):
    #print(i)

    fname = name[i] + "_y45718mk"+ ".txt"
    outf = open(fname, "w")
    #outf.write(str(result[i]))
    outf.write(str(count[i]))
    outf.write("\n")
    outf.close()
