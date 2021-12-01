import sys,os 

#Function to add a teams score:
def teamTotal(whichteam):	 
	total = 0
	for h in whichteam: 
		if h == 't': 
			total = total + 5 
		elif h == 'c': 
			total = total + 2 
		elif h == 'p': 
			total = total + 3 
		elif h == 'd': 
			total = total + 3 

	return total		
	#print(total)


insertFolder = sys.argv[1] 
prep = os.listdir(insertFolder) 
os.mkdir(sys.argv[2])
for q in prep:
	e = insertFolder + "/" + q 
	with open(e,'r') as livescore:
		data1 = livescore.readlines() 
		data = data1[0] 
		
		v = len(data) 

		team1 = [] 
		team2 = []

		x = 0 
		z = 0
		for x in range(int(v/3)):
			event = data[z+0:z+3]
			if event[0:2] == "T1": 
				team1.append(event[2])   
			else:	
				team2.append(event[2]) 
			z = z + 3	 
			

		
					
		teamTotal(team1) 
		teamTotal(team2)

		endTotal = str(teamTotal(team1)) + ":" + str(teamTotal(team2)) 
	#print(endTotal)  

	#creating output
	fix = q.replace('.txt','')
	outputFolder = sys.argv[2] + "/" + fix + "_m01964ua" + ".txt"
	outputFile = open(outputFolder, 'w')
	outputFile.write(endTotal)
	