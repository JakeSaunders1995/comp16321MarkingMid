import sys
arguments = sys.argv
print(arguments)

f=open('teamGoals.txt','r')
content = f.read()

T1Score = ((content.count('T1t'))*5)+((content.count('T1c'))*2)+((content.count('T1p'))*3)+((content.count('T1d'))*3)

T2Score = ((content.count('T2t'))*5)+((content.count('T2c'))*2)+((content.count('T2p'))*3)+((content.count('T2d'))*3)

game_results = str(T1Score)+':'+str(T2Score)

# input_file = 'game_results.txt'
input_file = arguments[1]

output_file = arguments[2]

with open(output_file,'w') as o:
	o.write(game_results)
	
