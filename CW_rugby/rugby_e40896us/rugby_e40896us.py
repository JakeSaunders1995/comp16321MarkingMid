import sys, os
for file in os.listdir(sys.argv[1]):
	with open(os.path.join(sys.argv[1], file)) as rugby_score:
		stats = rugby_score.readlines()

	individStats = stats[0].split('T')
	individStats.pop(0)

	def scoreTypes(letter):
		scoreAmount = 0
		if(letter == "t"):
			scoreAmount = 5
		elif(letter =="c"):
			scoreAmount = 2
		elif(letter == "p"):
			scoreAmount = 3
		elif(letter == "d"):
			scoreAmount = 3
		return scoreAmount


	team1 = 0
	team2 = 0
	for x in individStats:
		scoreAmount = scoreTypes(x[1])
		if(str(1) in x):
			team1 = team1 + scoreAmount
		else:
			team2 = team2 + scoreAmount
	finalRatio = str(team1) + ":" + str(team2)
	if(team1>team2): print("Team 1 is the winner!")
	elif(team2>team1): print("Team 2 is the winner!")
	else: print("It's a draw!")

	for outputFile in os.listdir(sys.argv[2]):
		correspondFile = os.path.splitext(file)[0] + "_e40896us"
		if(correspondFile == os.path.splitext(outputFile)[0]):
			with open(os.path.join(sys.argv[2], outputFile), 'w') as endStats:
				endStats.write(finalRatio)

