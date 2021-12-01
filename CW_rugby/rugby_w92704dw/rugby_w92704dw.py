import sys
import os

def scorelist(string):
    parsed = []
    
    for i in range((int(len(string)/3))):
        temp = string[3*i:(3*i)+3]
        parsed.append(temp)

    return parsed

def ratio(lists):
    t1 = 0
    t2 = 0

    temp = 0

    for i in lists:
        if(i[2] == 't'):
            temp = 5
        elif(i[2] == 'c'):
            temp = 2
        elif(i[2] == 'p'):
            temp = 3
        elif(i[2] == 'd'):
            temp = 3

        if(i[1] == '1'):
            t1 += temp
        elif(i[1] == '2'):
            t2 += temp

    return (str(t1) + ":" + str(t2))

def win(string):
    t1 = 0
    t2 = 0

    for i in range(len(string)):
        if(string[i] == ':'):
            t1 = int(string[0:i])
            t2 = int(string[i + 1:len(string)])
            break

    if(t1 > t2):
        return "Team 1 wins"
    if(t2 > t1):
        return "Team 2 wins"
    else:
        return "Both teams draw"

def main():
    files = os.listdir(sys.argv[1])
    for i in files:
        comp = ''

        for k in range(len(i)):
            if(i[k] == '.' or k == len(i) - 1):
                comp = sys.argv[2] + '/' + i[:k] + '_w92704dw.txt'
                break
      
        i = sys.argv[1] + '/' + i
        with open(i, 'r') as input:
            scores = (input.read()).replace(" ", "")
            scores = scores.replace('\n', '')
            
        main = scorelist(scores)

        with open(comp, 'w') as output:
            output.write(ratio(main))

        #with open(comp, 'r') as output:
            #print(comp + ':')
            #print(win(output.read()) + '\n')

main()

