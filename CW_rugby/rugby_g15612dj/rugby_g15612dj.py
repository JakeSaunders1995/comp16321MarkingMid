import sys
import os
def RUGBY(st):
	goals = st.split('T')
	team1 = []
	team2 = []
	while '' in goals:
		goals.remove('')
	for item in goals:
		if item[0] == '1':
			team1.append(item[1])
		elif item[0] == '2':
			team2.append(item[1])
	mydic = {'t':5,'c':2,'p':3,'d':3} 
	team1 = sum([mydic[x] for x in team1])
	team2 = sum([mydic[x] for x in team2])
	return str(str(team1)+':'+str(team2))


















owd = os.getcwd()
try :
	os.chdir(sys.argv[2])
except:
	os.mkdir(sys.argv[2])
	os.chdir(sys.argv[2])
outputfolderpath = os.getcwd()
try:
	os.chdir(sys.argv[1])
except:
	os.chdir(owd+"/"+sys.argv[1])
	print('relative folderpath used as argument[1]')
inputfolderpath = os.getcwd()

for cwd, dirnames, files in os.walk(os.getcwd()):
	for filename in files:
		fileIn = open(cwd+"/"+filename,'r').read()
		output = RUGBY(fileIn)
		newfilename = filename[:-3]+'_g15612dj'
		os.chdir(outputfolderpath)
		newfile = open(newfilename,'w')
		newfile.write(output)
		newfile.close()
