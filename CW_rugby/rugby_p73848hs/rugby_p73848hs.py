import sys
import os
username = "_p73848hs"

files=os.listdir(sys.argv[1].strip("./"))
for filename in files:
#opens file and saves content in scores
	file=open(sys.argv[1].strip("./")+"/"+filename)
	scores=file.read()
	file.close()


#splits the string scores wherever there is a T
	scores=scores.split('T')
	scores.remove('')  #first element would be empty so remove that


#splits the list scores into two lists
#team1 stores the scores of T1
#team2 stores the scores of T2
	team1=[]
	team2=[]
	for x in range (len(scores)):
	    if scores[x][0]=="1":
	        team1.append(scores[x][1])
	    else:
	        team2.append(scores[x][1])
	
	
	
#this function takes the string format of the score and returns the numerical points
	def scorenum(score):
	    if score=="t":
	        return 5
	    elif score=="c":
	        return 2
	    elif score=="p":
	        return 3
	    elif score=="d":
	        return 3
	    else:
	        print("error")
	

#this turns both teams scores into points saved in score1 for team1 and score2 for team2        
	score1=0
	score2=0
	for current_score in range(len(team1)):
	    score1 += scorenum(team1[current_score])
	for current_score in range(len(team2)):
	    score2 += scorenum(team2[current_score])


	file=open(sys.argv[2].strip("./")+"/"+ filename + username ,"w")

	file.writelines(str(score1)+"\n")
	file.writelines(str(score2))
	file.close()
