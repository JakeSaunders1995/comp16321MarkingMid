import argparse, os, sys, re


t = "t"
c = "c"
p = "p"
d = "d"
scoreofT1 = 0
scoreofT2 = 0
score1 = ("")
score2 = ("")
totalscore1 = 0
totalscore2 = 0

path = sys.argv[1]
outputpath = sys.argv[2]
os.mkdir(outputpath)
if os.path.exists(path):
	inputfile = os.listdir(path)
	print(inputfile)
	for file in inputfile:

		
		os.chdir(outputpath)
		outputfilename = 'text_file' + file[9] + '_r42421yz.txt'
		fp = open(outputfilename,'w')


		filepath = os.path.join(path,file)
		with open (filepath) as f:
			contentofInput = f.read()
			print(contentofInput)
			print(type(contentofInput))
			#team1
			Team1 = "T1t|T1c|T1p|T1d"
			Team1score = re.findall(Team1, contentofInput)
			print("Team1 ",Team1score)
			
			
			
		
			#team2
			Team2 = "T2t|T2c|T2p|T2d"
			Team2score = re.findall(Team2, contentofInput)
			print("Team2 ",Team2score)

			for i in range(0,len(Team1score)):
				score1 += Team1score[i][2]
			print(score1)
			for i in range(0,len(score1)):
				if score1[i] == t:
					totalscore1 += 5
				elif score1[i] == c:
					totalscore1 += 2
				elif score1[i] == p:
					totalscore1 +=3
				elif score1[i] == d:
					totalscore1 += 3
			print("score of T1 is: ",totalscore1)



			for i in range(0,len(Team2score)):
				score2 += Team2score[i][2]
			print(score2)
			for i in range(0,len(score2)):
				if score2[i] == t:
					totalscore2 += 5
				elif score2[i] == c:
					totalscore2 += 2
				elif score2[i] == p:
					totalscore2 +=3
				elif score2[i] == d:
					totalscore2 += 3
			print("score of T2 is: ",totalscore2)
			print(totalscore1,":",totalscore2)
			winner = str(totalscore1)+":"+str(totalscore2)
			print ( winner)

			fp.write(winner)
			fp.close


			score1 = ""
			totalscore1 = 0
			score2 = ""
			totalscore2 = 0

