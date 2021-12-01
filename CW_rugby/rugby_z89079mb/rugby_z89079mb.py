import sys
import os 
def adding_scores(last_letter):
    for i in scores:
        if i[0] == last_letter:
            return i[1]

directory = sys.argv[1]
all_files = []
for filename in os.listdir(directory):
    input_file = os.path.join(directory, filename)
    if os.path.isfile(input_file):
        all_files.append(input_file)
scores = [['t',5],['c',2],['p',3],['d',3]]

for a in all_files:
    T1 = 0
    T2 = 0
    with open(a) as file:
        file= file.read()
    data = [file[i:i+3] for i in range(0,len(file),3)]
    for i in data:
        if i[0:2] == 'T1': 
            T1 += adding_scores(i[-1])
        else: 
            T2 += adding_scores(i[-1])

    if T1>T2:
        print('Team 1 is the winner!')
    elif T2>T1:
        print('Team 2 is the winner!')        
    else:
        print("It's a draw.")
    filename = a[:-4]+'_z89079mb.txt'
    filename = filename.replace(sys.argv[1],sys.argv[2])
    with open(filename,'w') as fi:
        fi.write('%s:%s' % (T1,T2))
