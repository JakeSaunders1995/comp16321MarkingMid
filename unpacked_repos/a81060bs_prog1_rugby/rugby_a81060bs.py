# NOTE: Write down the code to input txt files. asighn the txt file to points.

import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

f = open(sys.argv[1], 'r')
points = f.read()
z = open(sys.argv[2], 'w')

# points = str("T1tT2pT2pT1pT1d")
list =[]# the output is ['T1t', 'T2p', 'T2p', 'T1p', 'T1d']
teamone = int()
teamtwo = int()

for x in range(0, len(points), 3):
    list.append(points[x: x + 3])
# NOTE: the code above makes list froma text file.


for y in list:
    if y == 'T1t':
        teamone += 5
    elif y == 'T2t':
        teamtwo +=5
    elif y == 'T1c':
        teamone +=2
    elif y == 'T2c':
        teamtwo +=2
    elif y == 'T1p':
        teamone +=3
    elif y == 'T2p':
        teamtwo +=3
    elif y == 'T1d':
        teamone +=3
    elif y == 'T2d':
        teamtwo +=3
# NOTE:  The code above converts list into points

x = str(teamone) + ':' + str(teamtwo)
output_file = z.write(x)
# NOTE: determines whos the winner.
if teamone > teamtwo:
    winner1 = str("Team One is a winner! ")
    # output_file = z.write(winner1)
    print('Team Two is a winner! ')

else:
    winner2 = str('Team Two is a winner! ')
    # output_file = z.write(winner2)
    print('Team Two is a winner! ')



print(x)

# x = str(teamone) + ':' + str(teamtwo)
